# AI Wiki Quiz Generator - Setup Instructions

## Prerequisites Installation

### 1. Install PostgreSQL

**Download and Install:**
1. Go to https://www.postgresql.org/download/windows/
2. Download the Windows installer (PostgreSQL 15 or later)
3. Run the installer and use these settings:
   - Password for postgres user: **postgres**
   - Port: **5432**
   - Locale: Default
   - Install all components when asked

**After Installation:**
1. PostgreSQL should start automatically as a Windows service
2. Verify it's running:
   - Open Services (Windows + R, type `services.msc`)
   - Look for "postgresql-x64-15" (or similar)
   - Status should be "Running"

### 2. Create the Database

**Option 1: Using pgAdmin (GUI)**
1. Open pgAdmin (installed with PostgreSQL)
2. Connect to the PostgreSQL server (password: postgres)
3. Right-click on "Databases" → "Create" → "Database"
4. Name: **quizmaster**
5. Click "Save"

**Option 2: Using Command Line**
```bash
# Add PostgreSQL to PATH or use full path
"C:\Program Files\PostgreSQL\15\bin\psql.exe" -U postgres -c "CREATE DATABASE quizmaster;"
```

## Backend Setup

### 1. Navigate to Backend Directory
```bash
cd c:\Users\sumanth\Downloads\QuizMasterAI\QuizMasterAI\backend
```

### 2. Verify Environment Variables
Check that `.env` file has:
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/quizmaster
GEMINI_API_KEY=AIzaSyDM-3UwgniXZruBojIoPoHpK1NvCaKPckY
```

### 3. Initialize Database
```bash
C:\Users\sumanth\Downloads\QuizMasterAI\QuizMasterAI\.venv\Scripts\python.exe init_db.py
```

### 4. Start Backend Server
```bash
C:\Users\sumanth\Downloads\QuizMasterAI\QuizMasterAI\.venv\Scripts\python.exe -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The backend will be available at: http://localhost:8000

## Frontend Setup

### 1. Navigate to Frontend Directory (New Terminal)
```bash
cd c:\Users\sumanth\Downloads\QuizMasterAI\QuizMasterAI\frontend
```

### 2. Start Frontend Development Server
```bash
npm run dev
```

The frontend will be available at: http://localhost:5173 or http://localhost:5000

## Testing the Application

1. Open your browser to the frontend URL
2. Click on "Generate Quiz" tab
3. Enter a Wikipedia URL (e.g., https://en.wikipedia.org/wiki/Artificial_intelligence)
4. Click "Generate Quiz"
5. Wait 10-30 seconds for the AI to process
6. View your generated quiz!
7. Check "Quiz History" tab to see all generated quizzes

## API Endpoints

- `GET /` - Health check
- `POST /generate_quiz` - Generate new quiz from Wikipedia URL
- `GET /history` - Get list of all quizzes
- `GET /quiz/{quiz_id}` - Get specific quiz details

## Troubleshooting

### PostgreSQL Connection Error
- Verify PostgreSQL service is running in Windows Services
- Check that port 5432 is not blocked
- Verify database "quizmaster" exists

### GEMINI_API_KEY Error
- Ensure your API key is valid
- Get a new key from: https://aistudio.google.com/app/apikey
- Update the `.env` file with your key

### Frontend Cannot Connect to Backend
- Ensure backend is running on port 8000
- Check CORS settings in main.py
- Verify frontend .env has correct API URL

## Project Structure

```
QuizMasterAI/
├── backend/
│   ├── database.py           # SQLAlchemy setup and Quiz model
│   ├── models.py             # Pydantic schemas for API and LLM
│   ├── scraper.py            # Wikipedia scraping functions
│   ├── llm_quiz_generator.py # LangChain + Gemini integration
│   ├── main.py               # FastAPI app and endpoints
│   ├── init_db.py            # Database initialization script
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # Environment variables
│
├── frontend/
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   │   ├── QuizDisplay.jsx
│   │   │   ├── HistoryTable.jsx
│   │   │   └── Modal.jsx
│   │   ├── tabs/             # Tab components
│   │   │   ├── GenerateQuizTab.jsx
│   │   │   └── HistoryTab.jsx
│   │   ├── services/
│   │   │   └── api.js        # API communication
│   │   ├── App.jsx           # Main React component
│   │   └── main.jsx          # React entry point
│   ├── package.json
│   └── .env                  # Frontend environment variables
│
└── .venv/                    # Python virtual environment
```

## Features

✅ AI-powered quiz generation using Google Gemini
✅ Wikipedia article scraping with clean content extraction
✅ 5-10 multiple-choice questions with varied difficulty
✅ Detailed explanations for each answer
✅ PostgreSQL database for persistent storage
✅ Quiz history with search and filter
✅ Clean, responsive UI with Tailwind CSS
✅ Real-time quiz generation feedback

## Tech Stack

**Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL, LangChain, Google Gemini
**Frontend:** React, Vite, Tailwind CSS, Axios
**AI:** Google Gemini Pro via LangChain with JsonOutputParser

---

Built with ❤️ using AI and modern web technologies