import os
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def generate_quiz(article_title: str, article_content: str) -> dict:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        temperature=0.4,
        google_api_key=api_key
    )
    
    prompt_template = """You are an AI quiz creator. 
Based on the Wikipedia article below, generate a JSON object with the following structure:

{{
  "title": "Quiz title based on the article",
  "summary": "Brief 2-3 sentence summary of the article",
  "quiz": [
    {{
      "question": "A clear, specific question about the article content",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "answer": "The correct option (exact text from options)",
      "difficulty": "easy or medium or hard",
      "explanation": "Brief explanation of why this is the correct answer"
    }}
  ],
  "related_topics": ["Topic 1", "Topic 2", "Topic 3"]
}}

Generate 5-10 multiple-choice questions with varied difficulty levels. Make sure:
- Questions are factual and based on the article content
- All 4 options are plausible but only one is correct
- The "answer" field exactly matches one of the options
- Explanations are educational and concise
- Topics cover different aspects of the article

Article Title: {title}

Article Content: {content}

Return ONLY the JSON object, no additional text or markdown formatting."""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["title", "content"]
    )
    
    chain = prompt | model | StrOutputParser()
    
    result = chain.invoke({
        "title": article_title,
        "content": article_content[:4000]
    })
    
    result_clean = result.strip()
    if result_clean.startswith("```json"):
        result_clean = result_clean[7:]
    if result_clean.startswith("```"):
        result_clean = result_clean[3:]
    if result_clean.endswith("```"):
        result_clean = result_clean[:-3]
    result_clean = result_clean.strip()
    
    try:
        quiz_data = json.loads(result_clean)
        return quiz_data
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse LLM response as JSON: {str(e)}\nResponse: {result_clean[:500]}")
