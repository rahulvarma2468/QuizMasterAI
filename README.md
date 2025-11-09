# AI Wiki Quiz Generator

A full-stack web application that generates intelligent, educational quizzes from Wikipedia articles using Google's Gemini AI. Simply provide a Wikipedia URL, and the app will scrape the article, analyze its content, and create a comprehensive quiz with multiple-choice questions, difficulty levels, and detailed explanations.

## 🎯 Features

- **AI-Powered Quiz Generation**: Uses Google Gemini Pro via LangChain with JsonOutputParser for structured output
- **Wikipedia Article Scraping**: Automatically extracts clean content, removing boilerplate, references, and tables
- **Intelligent Question Design**: Generates 5-10 multiple-choice questions with varied difficulty levels (easy, medium, hard)
- **Detailed Explanations**: Each question includes an educational explanation of the correct answer
- **Persistent Storage**: All quizzes saved to PostgreSQL database for future reference
- **Quiz History**: View and revisit all previously generated quizzes
- **Modern UI**: Clean, responsive interface built with React and Tailwind CSS
- **Real-time Feedback**: Loading states and error handling for better UX

## 🛠️ Tech Stack

### Backend
- **Python 3.10+**: Core programming language
- **FastAPI**: High-performance Python web framework
- **SQLAlchemy**: Database ORM for PostgreSQL
- **PostgreSQL**: Relational database for quiz storage
- **LangChain**: Framework for LLM integration with JsonOutputParser
- **Google Gemini AI**: AI model for quiz generation
- **BeautifulSoup**: Web scraping library
- **Pydantic**: Data validation and settings management

### Frontend
- **React 18**: JavaScript library for building user interfaces
- **Vite**: Next-generation frontend build tool
- **Tailwind CSS**: Utility-first CSS framework
- **Axios**: HTTP client for API requests
- **React Router**: Client-side routing

## 📁 Project Structure

```
ai-quiz-generator/
├── backend/
│   ├── venv/                       # Python Virtual Environment
│   ├── database.py                 # SQLAlchemy setup and Quiz model
│   ├── models.py                   # Pydantic Schemas for LLM output (QuizOutput)
│   ├── scraper.py                  # Functions for fetching and cleaning Wikipedia HTML
│   ├── llm_quiz_generator.py       # LangChain setup, prompt templates, and chain logic
│   ├── main.py                     # FastAPI application and API endpoints
│   ├── init_db.py                  # Database initialization script
│   ├── requirements.txt            # List of all Python dependencies
│   └── .env                        # API keys and environment variables
│
├── frontend/
│   ├── src/
│   │   ├── components/             # Reusable UI parts
│   │   │   ├── QuizDisplay.jsx     # Reusable component for rendering quiz data
│   │   │   ├── HistoryTable.jsx    # Quiz history table component
│   │   │   └── Modal.jsx           # Generic modal component
│   │   ├── services/
│   │   │   └── api.js              # Functions for communicating with FastAPI backend
│   │   ├── tabs/
│   │   │   ├── GenerateQuizTab.jsx # Quiz generation tab
│   │   │   └── HistoryTab.jsx      # Quiz history tab
│   │   ├── App.jsx                 # Main React component, handles routing
│   │   ├── main.jsx                # React entry point
│   │   └── index.css               # Tailwind directives and custom styles
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── .env                        # Frontend environment variables
│
├── .venv/                          # Python virtual environment
├── SETUP_INSTRUCTIONS.md           # Detailed setup guide
└── README.md                       # This file
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL 15+
- Google Gemini API Key (from https://aistudio.google.com/app/apikey)

### Backend Setup

1. **Install PostgreSQL**:
   - Download from https://www.postgresql.org/download/windows/
   - Use password: `postgres`
   - Use port: `5432`

2. **Create Database**:
   ```bash
   psql -U postgres -c "CREATE DATABASE quizmaster;"
   ```

3. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

4. **Install Python dependencies** (already done via virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**:
   Create/edit `.env` file:
   ```
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/quizmaster
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

6. **Initialize database**:
   ```bash
   python init_db.py
   ```

7. **Run the backend server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies** (already done):
   ```bash
   npm install
   ```

3. **Configure environment**:
   Create/edit `.env` file:
   ```
   VITE_API_BASE_URL=http://localhost:8000
   ```

4. **Run the development server**:
   ```bash
   npm run dev
   ```

   The app will be available at `http://localhost:5173` or `http://localhost:5000`

## 📖 Usage Guide

### Generating a Quiz

1. Open the application in your browser
2. Navigate to the "Generate Quiz" tab (default view)
3. Enter a Wikipedia article URL (e.g., `https://en.wikipedia.org/wiki/Artificial_intelligence`)
4. Click "Generate Quiz"
5. Wait for the AI to process the article (usually 10-30 seconds)
6. View your generated quiz with questions, answers, and explanations

### Viewing Quiz History

1. Click on the "Quiz History" tab
2. Browse all previously generated quizzes in the table
3. Click "View Details" on any quiz to see its full content in a modal
4. Click on the Wikipedia URL to revisit the original article

## 🔌 API Endpoints

### `POST /generate_quiz`
Generate a new quiz from a Wikipedia URL.

**Request Body**:
```json
{
  "url": "https://en.wikipedia.org/wiki/Python_(programming_language)"
}
```

**Response**:
```json
{
  "id": 1,
  "url": "https://en.wikipedia.org/wiki/Python_(programming_language)",
  "title": "Python (programming language)",
  "date_generated": "2025-11-09T14:30:00",
  "quiz_data": {
    "title": "Python Programming Quiz",
    "summary": "Python is a high-level programming language...",
    "quiz": [
      {
        "question": "What year was Python first released?",
        "options": ["1989", "1991", "1995", "2000"],
        "answer": "1991",
        "difficulty": "medium",
        "explanation": "Python was first released in 1991 by Guido van Rossum."
      }
    ],
    "related_topics": ["Programming", "Software Development", "Guido van Rossum"]
  }
}
```

### `GET /history`
Retrieve all quiz history.

**Response**:
```json
[
  {
    "id": 1,
    "url": "https://en.wikipedia.org/wiki/...",
    "title": "Article Title",
    "date_generated": "2025-11-09T14:30:00"
  }
]
```

### `GET /quiz/{quiz_id}`
Retrieve a specific quiz by ID.

**Response**: Same structure as `POST /generate_quiz`

## 🗄️ Database Schema

### Quiz Table
```sql
CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    url VARCHAR(500) NOT NULL,
    title VARCHAR(500) NOT NULL,
    date_generated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    scraped_content TEXT,
    full_quiz_data TEXT  -- JSON stored as text
);
```

## 🤖 LLM Integration

The application uses LangChain's `JsonOutputParser` with a Pydantic schema (`QuizOutput`) to ensure the LLM returns valid, structured JSON. The prompt template guides Gemini Pro to generate:

- Quiz title and summary
- 5-10 multiple-choice questions
- Four options per question
- Difficulty levels (easy/medium/hard)
- Explanations for correct answers
- Related topics

## 🧪 Testing

### Sample Wikipedia URLs
- https://en.wikipedia.org/wiki/Artificial_intelligence
- https://en.wikipedia.org/wiki/Python_(programming_language)
- https://en.wikipedia.org/wiki/Machine_learning
- https://en.wikipedia.org/wiki/Quantum_computing
- https://en.wikipedia.org/wiki/Climate_change

## 🐛 Troubleshooting

### Backend Issues

**Error: "GEMINI_API_KEY environment variable not set"**
- Ensure you've set the GEMINI_API_KEY in `.env`
- Verify the key is valid at https://aistudio.google.com/app/apikey

**Error: "Failed to fetch Wikipedia article"**
- Verify the URL is a valid Wikipedia article
- Check your internet connection
- Ensure the article exists and is publicly accessible

**Database connection errors**
- Verify DATABASE_URL is correctly configured
- Ensure PostgreSQL is running and accessible
- Check database credentials
- Verify database "quizmaster" exists

### Frontend Issues

**API connection errors**
- Ensure the backend server is running on port 8000
- Check that CORS is properly configured
- Verify the VITE_API_BASE_URL in `frontend/.env`

**Styling issues**
- Ensure Tailwind CSS is properly configured
- Run `npm install` to install all dependencies
- Check that `postcss.config.js` and `tailwind.config.js` exist

## 🔮 Future Enhancements

- Interactive "Take Quiz" mode with answer submission and scoring
- Quiz filtering and search by title, date, or difficulty
- Export quizzes to PDF or JSON
- Quiz editing capability to modify generated questions
- User analytics dashboard with statistics
- Support for multiple languages
- Integration with other knowledge sources beyond Wikipedia
- User authentication and personal quiz collections

## 📄 License

This project is open-source and available for educational purposes.

## 🙏 Credits

- **AI Model**: Google Gemini Pro
- **LLM Framework**: LangChain
- **Content Source**: Wikipedia
- **UI Framework**: React + Tailwind CSS
- **Backend**: FastAPI

---

**Built with ❤️ for educational purposes**

A full-stack web application that generates intelligent quizzes from Wikipedia articles using Google's Gemini AI. Simply provide a Wikipedia URL, and the app will scrape the article, analyze its content, and create a comprehensive quiz with multiple-choice questions, difficulty levels, and detailed explanations.

## Features

- **AI-Powered Quiz Generation**: Uses Google Gemini 2.0 Flash via LangChain to create contextual quizzes
- **Wikipedia Article Scraping**: Automatically extracts clean content from any Wikipedia article
- **Intelligent Question Design**: Generates 5-10 multiple-choice questions with varying difficulty levels
- **Detailed Explanations**: Each question includes an educational explanation of the correct answer
- **Persistent Storage**: All quizzes are saved to PostgreSQL database for future reference
- **Quiz History**: View and revisit all previously generated quizzes
- **Modern UI**: Clean, responsive interface built with React and Tailwind CSS

## Tech Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **SQLAlchemy**: Database ORM for PostgreSQL
- **LangChain**: Framework for LLM integration
- **Google Gemini AI**: AI model for quiz generation
- **BeautifulSoup**: Web scraping library
- **PostgreSQL**: Relational database for quiz storage

### Frontend
- **React**: JavaScript library for building user interfaces
- **Vite**: Next-generation frontend build tool
- **Tailwind CSS**: Utility-first CSS framework
- **Axios**: HTTP client for API requests

## Project Structure

```
.
├── backend/
│   ├── main.py                 # FastAPI app with endpoints
│   ├── database.py             # SQLAlchemy database setup
│   ├── scraper.py              # Wikipedia scraper
│   ├── llm_quiz_generator.py   # Gemini quiz generator
│   ├── models.py               # Pydantic schemas
│   └── requirements.txt        # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/         # Reusable React components
│   │   │   ├── QuizDisplay.jsx
│   │   │   ├── HistoryTable.jsx
│   │   │   └── Modal.jsx
│   │   ├── tabs/               # Tab components
│   │   │   ├── GenerateQuizTab.jsx
│   │   │   └── HistoryTab.jsx
│   │   ├── services/           # API service layer
│   │   │   └── api.js
│   │   ├── App.jsx             # Main app component
│   │   └── index.css           # Tailwind styles
│   ├── package.json
│   └── vite.config.js
└── sample_data/
    ├── example_urls.txt        # Sample Wikipedia URLs
    └── example_quiz_output.json # Sample quiz structure
```

## Setup Instructions

### Prerequisites
- Python 3.11+
- Node.js 20+
- PostgreSQL database
- Google AI API Key (from https://aistudio.google.com/app/apikey)

### Backend Setup

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file or set the following environment variables:
   ```
   DATABASE_URL=postgresql://user:password@host:port/dbname
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Run the backend server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies**:
   ```bash
   npm install
   ```

3. **Run the development server**:
   ```bash
   npm run dev
   ```

   The app will be available at `http://localhost:5000`

## Usage Guide

### Generating a Quiz

1. Open the application in your browser
2. Navigate to the "Generate Quiz" tab (default view)
3. Enter a Wikipedia article URL (e.g., `https://en.wikipedia.org/wiki/Artificial_intelligence`)
4. Click "Generate Quiz"
5. Wait for the AI to process the article (usually 10-30 seconds)
6. View your generated quiz with questions, answers, and explanations

### Viewing Quiz History

1. Click on the "Quiz History" tab
2. Browse all previously generated quizzes in the table
3. Click "View Details" on any quiz to see its full content in a modal
4. Click on the Wikipedia URL to revisit the original article

## API Endpoints

### `POST /generate_quiz`
Generate a new quiz from a Wikipedia URL.

**Request Body**:
```json
{
  "url": "https://en.wikipedia.org/wiki/Python_(programming_language)"
}
```

**Response**:
```json
{
  "id": 1,
  "url": "https://en.wikipedia.org/wiki/Python_(programming_language)",
  "title": "Python (programming language)",
  "date_generated": "2025-11-09T14:30:00",
  "quiz_data": {
    "title": "Python Programming Quiz",
    "summary": "Python is a high-level programming language...",
    "quiz": [...],
    "related_topics": [...]
  }
}
```

### `GET /history`
Retrieve all quiz history.

**Response**:
```json
[
  {
    "id": 1,
    "url": "https://en.wikipedia.org/wiki/...",
    "title": "Article Title",
    "date_generated": "2025-11-09T14:30:00"
  }
]
```

### `GET /quiz/{id}`
Retrieve a specific quiz by ID.

**Response**: Same structure as `POST /generate_quiz`

## Database Schema

### Quiz Table
```sql
CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    url VARCHAR(500) NOT NULL,
    title VARCHAR(500) NOT NULL,
    date_generated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    scraped_content TEXT,
    full_quiz_data TEXT
);
```

## LLM Prompt Structure

The application uses a carefully crafted prompt for Gemini to ensure high-quality quiz generation:

```
You are an AI quiz creator. 
Based on the Wikipedia article below, generate JSON with:
{
  "title": "Quiz title",
  "summary": "Brief summary",
  "quiz": [
    {
      "question": "Question text",
      "options": ["A", "B", "C", "D"],
      "answer": "Correct option",
      "difficulty": "easy|medium|hard",
      "explanation": "Why this is correct"
    }
  ],
  "related_topics": ["Topic 1", "Topic 2"]
}
```

## Sample Data

The `sample_data/` folder contains:
- **example_urls.txt**: 10+ curated Wikipedia URLs for testing
- **example_quiz_output.json**: Sample quiz structure showing expected format

## Troubleshooting

### Backend Issues

**Error: "GEMINI_API_KEY environment variable not set"**
- Ensure you've set the GEMINI_API_KEY environment variable
- Verify the key is valid at https://aistudio.google.com/app/apikey

**Error: "Failed to fetch Wikipedia article"**
- Verify the URL is a valid Wikipedia article
- Check your internet connection
- Ensure the article exists and is publicly accessible

**Database connection errors**
- Verify DATABASE_URL is correctly configured
- Ensure PostgreSQL is running and accessible
- Check database credentials

### Frontend Issues

**API connection errors**
- Ensure the backend server is running on port 8000
- Check that CORS is properly configured
- Verify the API_BASE_URL in `frontend/src/services/api.js`

**Styling issues**
- Ensure Tailwind CSS is properly configured
- Run `npm install` to install all dependencies
- Check that `postcss.config.js` and `tailwind.config.js` exist

## Development Notes

### Running Both Servers Simultaneously

You can use two terminal windows:

**Terminal 1 (Backend)**:
```bash
cd backend && uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Terminal 2 (Frontend)**:
```bash
cd frontend && npm run dev
```

### Making Changes

- **Backend**: FastAPI auto-reloads on file changes
- **Frontend**: Vite hot-reloads React components automatically
- **Database schema changes**: Restart the backend to apply migrations

## Future Enhancements

- Interactive "Take Quiz" mode that hides answers until submission
- Quiz filtering and search by title, date, or difficulty
- Export quizzes to PDF or JSON
- Quiz editing capability to modify generated questions
- User analytics dashboard with statistics
- Support for multiple languages
- Integration with other knowledge sources beyond Wikipedia

## License

This project is open-source and available for educational purposes.

## Credits

- **AI Model**: Google Gemini 2.0 Flash
- **LLM Framework**: LangChain
- **Content Source**: Wikipedia
- **UI Framework**: React + Tailwind CSS
- **Backend**: FastAPI

---

**Built with ❤️ for DeepKlarity**
