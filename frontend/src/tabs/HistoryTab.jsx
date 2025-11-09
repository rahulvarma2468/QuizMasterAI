import React, { useState, useEffect } from 'react';
import { getHistory, getQuiz } from '../services/api';
import HistoryTable from '../components/HistoryTable';
import Modal from '../components/Modal';
import QuizDisplay from '../components/QuizDisplay';

const HistoryTab = () => {
  const [quizzes, setQuizzes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [selectedQuiz, setSelectedQuiz] = useState(null);
  const [modalOpen, setModalOpen] = useState(false);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const data = await getHistory();
      setQuizzes(data);
    } catch (err) {
      setError(typeof err === 'string' ? err : 'Failed to load quiz history');
    } finally {
      setLoading(false);
    }
  };

  const handleViewDetails = async (quizId) => {
    try {
      const quizData = await getQuiz(quizId);
      setSelectedQuiz(quizData);
      setModalOpen(true);
    } catch (err) {
      alert('Failed to load quiz details');
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center py-12">
        <svg className="animate-spin h-8 w-8 text-blue-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
        {error}
      </div>
    );
  }

  return (
    <div>
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800">Quiz History</h2>
        <p className="text-gray-600 mt-1">View all previously generated quizzes</p>
      </div>

      <HistoryTable quizzes={quizzes} onViewDetails={handleViewDetails} />

      <Modal isOpen={modalOpen} onClose={() => setModalOpen(false)}>
        {selectedQuiz && (
          <div>
            <div className="mb-4 pb-4 border-b">
              <h3 className="text-xl font-bold text-gray-800">{selectedQuiz.title}</h3>
              <p className="text-sm text-gray-600 mt-1">
                Generated on {new Date(selectedQuiz.date_generated).toLocaleDateString()}
              </p>
              <a
                href={selectedQuiz.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-blue-600 hover:text-blue-800 mt-1 inline-block"
              >
                View Original Article →
              </a>
            </div>
            <QuizDisplay quizData={selectedQuiz.quiz_data} />
          </div>
        )}
      </Modal>
    </div>
  );
};

export default HistoryTab;
