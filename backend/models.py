from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime

class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answer: str
    difficulty: str
    explanation: str

class QuizData(BaseModel):
    title: str
    summary: str
    quiz: List[QuizQuestion]
    related_topics: List[str]

class QuizGenerateRequest(BaseModel):
    url: str

class QuizResponse(BaseModel):
    id: int
    url: str
    title: str
    date_generated: datetime
    quiz_data: QuizData
    
    class Config:
        from_attributes = True

class QuizHistoryItem(BaseModel):
    id: int
    url: str
    title: str
    date_generated: datetime
    
    class Config:
        from_attributes = True
