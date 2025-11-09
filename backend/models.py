from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

# Pydantic models for LLM output structure
class QuizQuestion(BaseModel):
    """Model for a single quiz question"""
    question: str = Field(..., description="The question text")
    options: List[str] = Field(..., min_length=4, max_length=4, description="Four answer options")
    answer: str = Field(..., description="The correct answer (must match one option exactly)")
    difficulty: str = Field(..., description="Difficulty level: easy, medium, or hard")
    explanation: str = Field(..., description="Explanation of why the answer is correct")

class QuizOutput(BaseModel):
    """Complete quiz structure that the LLM must generate"""
    title: str = Field(..., description="Quiz title based on the article")
    summary: str = Field(..., description="Brief 2-3 sentence summary of the article")
    quiz: List[QuizQuestion] = Field(..., min_length=5, max_length=10, description="5-10 quiz questions")
    related_topics: List[str] = Field(..., description="List of related topics from the article")

# API Request/Response Models
class QuizGenerateRequest(BaseModel):
    """Request model for generating a new quiz"""
    url: str = Field(..., description="Wikipedia article URL")

class QuizResponse(BaseModel):
    """Response model for quiz data"""
    id: int
    url: str
    title: str
    date_generated: datetime
    quiz_data: QuizOutput
    
    class Config:
        from_attributes = True

class QuizHistoryItem(BaseModel):
    """Simplified model for quiz history list"""
    id: int
    url: str
    title: str
    date_generated: datetime
    
    class Config:
        from_attributes = True
