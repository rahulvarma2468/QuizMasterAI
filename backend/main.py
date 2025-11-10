from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import json
from typing import List

from database import get_db, init_db, Quiz
from models import QuizGenerateRequest, QuizResponse, QuizHistoryItem, QuizOutput
from scraper import scrape_wikipedia_article
from llm_quiz_generator import generate_quiz

# Initialize FastAPI application
app = FastAPI(
    title="AI Wiki Quiz Generator",
    description="Generate educational quizzes from Wikipedia articles using AI",
    version="1.0.0"
)

# Configure CORS to allow frontend communication
origins = [
    "http://localhost:5173",  # Local Vite dev server
    "http://localhost:5174",
    "https://*.vercel.app",   # All Vercel preview/production deployments
    "https://quizmasterai.onrender.com",  # Backend (for testing)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for easier deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """Initialize database tables on application startup"""
    init_db()
    print("Database initialized successfully")

@app.get("/")
async def root():
    """Root endpoint - API health check"""
    return {
        "message": "AI Wiki Quiz Generator API",
        "status": "running",
        "version": "1.0.0"
    }

@app.post("/generate_quiz", response_model=QuizResponse)
async def generate_quiz_endpoint(
    request: QuizGenerateRequest,
    db: Session = Depends(get_db)
):
    """
    Generate a new quiz from a Wikipedia URL.
    
    Steps:
    1. Scrape the Wikipedia article
    2. Generate quiz using LLM
    3. Save to database
    4. Return the generated quiz
    """
    try:
        # Step 1: Scrape Wikipedia article
        scraped_data = scrape_wikipedia_article(request.url)
        
        # Step 2: Generate quiz using LLM
        quiz_data = generate_quiz(scraped_data["title"], scraped_data["content"])
        
        # Step 3: Serialize quiz data to JSON string for database storage
        quiz_json = json.dumps(quiz_data)
        
        # Step 4: Create database record
        db_quiz = Quiz(
            url=request.url,
            title=scraped_data["title"],
            scraped_content=scraped_data["content"],
            full_quiz_data=quiz_json
        )
        
        db.add(db_quiz)
        db.commit()
        db.refresh(db_quiz)
        
        # Step 5: Return response with proper structure
        return QuizResponse(
            id=db_quiz.id,
            url=db_quiz.url,
            title=db_quiz.title,
            date_generated=db_quiz.date_generated,
            quiz_data=QuizOutput(**quiz_data)
        )
    
    except ValueError as e:
        # Handle validation and scraping errors
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate quiz: {str(e)}"
        )

@app.get("/history", response_model=List[QuizHistoryItem])
async def get_history(db: Session = Depends(get_db)):
    """
    Get list of all generated quizzes.
    
    Returns simplified quiz information for the history table.
    """
    try:
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
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch quiz history: {str(e)}"
        )

@app.get("/quiz/{quiz_id}", response_model=QuizResponse)
async def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    """
    Get a specific quiz by ID.
    
    Deserializes the stored JSON data and returns the full quiz structure.
    """
    try:
        # Query database for quiz
        quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
        
        if not quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")
        
        # Deserialize the JSON string back to dictionary
        quiz_data = json.loads(quiz.full_quiz_data)
        
        # Return full quiz response
        return QuizResponse(
            id=quiz.id,
            url=quiz.url,
            title=quiz.title,
            date_generated=quiz.date_generated,
            quiz_data=QuizOutput(**quiz_data)
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch quiz: {str(e)}"
        )
