import React from 'react';
import { BrowserRouter, Routes, Route, NavLink, Navigate } from 'react-router-dom';
import GenerateQuizTab from './tabs/GenerateQuizTab';
import HistoryTab from './tabs/HistoryTab';

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        <div className="container mx-auto px-4 py-8">
          <header className="mb-8">
            <h1 className="text-4xl font-bold text-gray-800 mb-2">
              DeepKlarity AI Wiki Quiz Generator
            </h1>
            <p className="text-gray-600">
              Generate intelligent quizzes from any Wikipedia article using AI
            </p>
          </header>

          <div className="mb-6 border-b border-gray-300 bg-white rounded-t-lg shadow-sm">
            <nav className="flex space-x-1">
              <NavLink
                to="/generate"
                className={({ isActive }) =>
                  `px-6 py-3 font-semibold transition-colors ${
                    isActive
                      ? 'text-blue-600 border-b-2 border-blue-600 bg-blue-50'
                      : 'text-gray-600 hover:text-gray-800 hover:bg-gray-50'
                  }`
                }
              >
                Generate Quiz
              </NavLink>
              <NavLink
                to="/history"
                className={({ isActive }) =>
                  `px-6 py-3 font-semibold transition-colors ${
                    isActive
                      ? 'text-blue-600 border-b-2 border-blue-600 bg-blue-50'
                      : 'text-gray-600 hover:text-gray-800 hover:bg-gray-50'
                  }`
                }
              >
                Quiz History
              </NavLink>
            </nav>
          </div>

          <main>
            <Routes>
              <Route path="/" element={<Navigate to="/generate" replace />} />
              <Route path="/generate" element={<GenerateQuizTab />} />
              <Route path="/history" element={<HistoryTab />} />
              <Route path="*" element={<Navigate to="/generate" replace />} />
            </Routes>
          </main>

          <footer className="mt-12 text-center text-gray-600 text-sm">
            <p>Powered by Google Gemini AI & Wikipedia</p>
          </footer>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
