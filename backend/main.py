from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import json
from typing import List

from database import get_db, init_db, Quiz
from models import QuizGenerateRequest, QuizResponse, QuizHistoryItem, QuizData
from scraper import scrape_wikipedia_article
from llm_quiz_generator import generate_quiz

app = FastAPI(title="DeepKlarity AI Wiki Quiz Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
async def root():
    return {"message": "DeepKlarity AI Wiki Quiz Generator API", "status": "running"}

@app.post("/generate_quiz", response_model=QuizResponse)
async def generate_quiz_endpoint(request: QuizGenerateRequest, db: Session = Depends(get_db)):
    try:
        scraped_data = scrape_wikipedia_article(request.url)
        
        quiz_data = generate_quiz(scraped_data["title"], scraped_data["content"])
        
        quiz_json = json.dumps(quiz_data)
        
        db_quiz = Quiz(
            url=request.url,
            title=scraped_data["title"],
            scraped_content=scraped_data["content"],
            full_quiz_data=quiz_json
        )
        
        db.add(db_quiz)
        db.commit()
        db.refresh(db_quiz)
        
        return QuizResponse(
            id=db_quiz.id,
            url=db_quiz.url,
            title=db_quiz.title,
            date_generated=db_quiz.date_generated,
            quiz_data=QuizData(**quiz_data)
        )
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate quiz: {str(e)}")

@app.get("/history", response_model=List[QuizHistoryItem])
async def get_history(db: Session = Depends(get_db)):
    quizzes = db.query(Quiz).order_by(Quiz.date_generated.desc()).all()
    return [
        QuizHistoryItem(
            id=quiz.id,
            url=quiz.url,
            title=quiz.title,
            date_generated=quiz.date_generated
        )
        for quiz in quizzes
    ]

@app.get("/quiz/{quiz_id}", response_model=QuizResponse)
async def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    
    quiz_data = json.loads(quiz.full_quiz_data)
    
    return QuizResponse(
        id=quiz.id,
        url=quiz.url,
        title=quiz.title,
        date_generated=quiz.date_generated,
        quiz_data=QuizData(**quiz_data)
    )
