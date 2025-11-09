import React, { useState } from 'react';
import { generateQuiz } from '../services/api';
import QuizDisplay from '../components/QuizDisplay';

const GenerateQuizTab = () => {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [quizData, setQuizData] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setQuizData(null);

    if (!url.trim()) {
      setError('Please enter a Wikipedia URL');
      return;
    }

    if (!url.includes('wikipedia.org')) {
      setError('Please enter a valid Wikipedia URL');
      return;
    }

    setLoading(true);

    try {
      const data = await generateQuiz(url);
      setQuizData(data.quiz_data);
    } catch (err) {
      setError(typeof err === 'string' ? err : 'Failed to generate quiz. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Generate New Quiz</h2>
        <div className="space-y-4">
          <div>
            <label htmlFor="url" className="block text-sm font-medium text-gray-700 mb-2">
              Wikipedia Article URL
            </label>
            <input
              type="text"
              id="url"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              placeholder="https://en.wikipedia.org/wiki/..."
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              disabled={loading}
            />
          </div>
          {error && (
            <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
              {error}
            </div>
          )}
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
          >
            {loading ? (
              <span className="flex items-center justify-center">
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Generating Quiz...
              </span>
            ) : (
              'Generate Quiz'
            )}
          </button>
        </div>
      </form>

      {quizData && <QuizDisplay quizData={quizData} />}
    </div>
  );
};

export default GenerateQuizTab;
