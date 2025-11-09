# DeepKlarity AI Wiki Quiz Generator - Project Documentation

## Project Overview

**Purpose**: A full-stack AI-powered web application that generates intelligent quizzes from Wikipedia articles using Google Gemini AI.

**Current State**: MVP complete with all core features implemented and working. Backend and frontend are both running and functional.

**Last Updated**: November 9, 2025

## Recent Changes

### November 9, 2025 - Initial Implementation & Completion
- Created complete backend with FastAPI, SQLAlchemy, and Gemini AI integration
- Implemented Wikipedia scraper using BeautifulSoup with proper error handling
- Built LangChain-based quiz generator with structured prompts
- Created React + Tailwind frontend with React Router for URL-based navigation
- Set up PostgreSQL database with Quiz model
- Configured workflows for both backend (port 8000) and frontend (port 5000)
- Added comprehensive README and sample data
- Implemented React Router with /generate and /history routes
- Fixed error handling to return appropriate HTTP status codes (400 for client errors)
- Successfully tested both servers - all features working properly

## Tech Stack

### Backend
- Python 3.11
- FastAPI (web framework)
- SQLAlchemy (ORM)
- PostgreSQL (database)
- LangChain + Google Gemini AI (quiz generation)
- BeautifulSoup (web scraping)

### Frontend
- React 18
- Vite (build tool)
- Tailwind CSS (styling)
- React Router (routing)
- Axios (API client)

## Project Architecture

### API Endpoints
- `POST /generate_quiz`: Scrapes Wikipedia + generates quiz + stores in DB
- `GET /history`: Returns all quiz history
- `GET /quiz/{id}`: Returns specific quiz by ID

### Database Schema
```
Quiz Table:
- id (primary key)
- url (Wikipedia URL)
- title (article title)
- date_generated (timestamp)
- scraped_content (full article text)
- full_quiz_data (JSON quiz data)
```

### Frontend Structure
- **GenerateQuizTab**: URL input form + quiz display
- **HistoryTab**: Table view with modal for quiz details
- **Components**: QuizDisplay, HistoryTable, Modal
- **Services**: API integration layer

## Environment Variables

Required secrets (already configured):
- `DATABASE_URL`: PostgreSQL connection string
- `GEMINI_API_KEY`: Google AI API key for quiz generation
- `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`: PostgreSQL credentials

## Workflows

### Backend Workflow
- **Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port 8000 --reload`
- **Port**: 8000
- **Type**: Console
- **Status**: Running

### Frontend Workflow
- **Command**: `cd frontend && npm run dev`
- **Port**: 5000
- **Type**: Webview
- **Status**: Running

## User Preferences

*No specific preferences recorded yet*

## Known Issues

*No known issues at this time - all features working as expected*

## Next Steps (Future Enhancements)

1. Add interactive "Take Quiz" mode that hides answers until submission
2. Implement quiz filtering and search functionality
3. Add quiz export (PDF/JSON download)
4. Create quiz editing capability
5. Build analytics dashboard with statistics
6. Support for additional knowledge sources beyond Wikipedia

## Development Notes

- All LSP warnings are minor type-related issues and don't affect functionality
- Backend uses Gemini 2.0 Flash model for optimal performance
- Frontend configured for Replit's proxy at 0.0.0.0:5000
- Database automatically initializes on startup
- CORS enabled for frontend-backend communication
