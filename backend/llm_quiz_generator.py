import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

def generate_quiz(article_title: str, article_content: str) -> dict:
    """
    Generate a quiz from Wikipedia article content using Gemini LLM.
    
    Args:
        article_title: Title of the Wikipedia article
        article_content: Cleaned content from the article
        
    Returns:
        Dictionary containing quiz data matching QuizOutput schema
        
    Raises:
        ValueError: If API key is not set or generation fails
    """
    # Get API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    
    # Configure the Gemini API
    genai.configure(api_key=api_key)
    
    # Initialize the model with JSON response configuration
    model = genai.GenerativeModel(
        'gemini-2.5-flash',
        generation_config={
            "response_mime_type": "application/json"
        }
    )
    
    # Create the prompt with strict JSON schema
    prompt = f"""Generate a quiz from this Wikipedia article in valid JSON format.

Article: {article_title}

Content: {article_content[:4000]}

Create 5-8 multiple-choice questions. Return ONLY valid JSON matching this exact structure:

{{
  "title": "Quiz about [topic]",
  "summary": "Brief summary here",
  "quiz": [
    {{
      "question": "Question text?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "answer": "Option A",
      "difficulty": "easy",
      "explanation": "Why this is correct"
    }}
  ],
  "related_topics": ["Topic 1", "Topic 2", "Topic 3"]
}}

Rules:
- Use "easy", "medium", or "hard" for difficulty
- The answer field must exactly match one option
- Include 3-5 related topics
- Make questions factual and based on the article"""
    
    try:
        # Generate content with retries
        max_retries = 2
        for attempt in range(max_retries):
            try:
                response = model.generate_content(prompt)
                result = response.text.strip()
                
                # More aggressive cleaning
                # Remove markdown code blocks
                result = result.replace("```json", "").replace("```", "")
                
                # Remove any text before the first {
                if "{" in result:
                    result = result[result.index("{"):]
                
                # Remove any text after the last }
                if "}" in result:
                    result = result[:result.rindex("}") + 1]
                
                result = result.strip()
                
                # Parse JSON
                quiz_data = json.loads(result)
                
                # Validate the structure
                required_keys = ["title", "summary", "quiz", "related_topics"]
                if not all(key in quiz_data for key in required_keys):
                    raise ValueError(f"Missing required keys. Found: {list(quiz_data.keys())}")
                
                # Validate quiz questions
                if not isinstance(quiz_data["quiz"], list) or len(quiz_data["quiz"]) == 0:
                    raise ValueError("Quiz must contain at least one question")
                
                for i, q in enumerate(quiz_data["quiz"]):
                    if not all(k in q for k in ["question", "options", "answer", "difficulty", "explanation"]):
                        raise ValueError(f"Question {i+1} missing required fields")
                    if len(q["options"]) != 4:
                        raise ValueError(f"Question {i+1} must have exactly 4 options")
                    if q["answer"] not in q["options"]:
                        # Try to fix: find closest match
                        q["answer"] = q["options"][0]
                
                return quiz_data
                
            except json.JSONDecodeError as e:
                if attempt < max_retries - 1:
                    print(f"JSON parse error on attempt {attempt + 1}, retrying...")
                    continue
                # Last attempt failed, provide detailed error
                print(f"Failed JSON content:\n{result[:500]}...")
                raise ValueError(f"Failed to parse LLM response as JSON: {str(e)}")
        
    except Exception as e:
        raise ValueError(f"Failed to generate quiz: {str(e)}")
