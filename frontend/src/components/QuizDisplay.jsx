import React, { useState } from 'react';

const QuizDisplay = ({ quizData, reviewMode = false }) => {
  const [userAnswers, setUserAnswers] = useState({});
  const [showResults, setShowResults] = useState(reviewMode); // Start in results mode if reviewMode is true

  const getDifficultyColor = (difficulty) => {
    switch (difficulty.toLowerCase()) {
      case 'easy':
        return 'bg-green-100 text-green-800';
      case 'medium':
        return 'bg-yellow-100 text-yellow-800';
      case 'hard':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  const handleOptionSelect = (questionIndex, option) => {
    if (!showResults && !reviewMode) {
      setUserAnswers({
        ...userAnswers,
        [questionIndex]: option
      });
    }
  };

  const handleSubmit = () => {
    if (Object.keys(userAnswers).length < quizData.quiz.length) {
      if (!window.confirm('You haven\'t answered all questions. Submit anyway?')) {
        return;
      }
    }
    setShowResults(true);
  };

  const handleRetake = () => {
    setUserAnswers({});
    setShowResults(false);
  };

  const calculateScore = () => {
    let correct = 0;
    quizData.quiz.forEach((question, index) => {
      if (userAnswers[index] === question.answer) {
        correct++;
      }
    });
    return correct;
  };

  const getOptionClass = (questionIndex, option, correctAnswer) => {
    if (!showResults) {
      // Quiz mode - show selected state
      if (userAnswers[questionIndex] === option) {
        return 'bg-blue-100 border-blue-500 border-2';
      }
      return 'bg-gray-50 border-gray-200 hover:bg-gray-100 cursor-pointer';
    } else {
      // Results mode - show correct/incorrect
      if (option === correctAnswer) {
        return 'bg-green-50 border-green-500 border-2 font-medium';
      }
      if (userAnswers[questionIndex] === option && option !== correctAnswer) {
        return 'bg-red-50 border-red-500 border-2';
      }
      return 'bg-gray-50 border-gray-200';
    }
  };

  return (
    <div className="space-y-6">
      <div className="bg-gradient-to-r from-blue-500 to-purple-600 text-white p-6 rounded-lg shadow-lg">
        <h2 className="text-3xl font-bold mb-2">{quizData.title}</h2>
        <p className="text-blue-100">{quizData.summary}</p>
        {showResults && !reviewMode && (
          <div className="mt-4 bg-white text-gray-800 p-4 rounded-lg">
            <p className="text-2xl font-bold">
              Score: {calculateScore()} / {quizData.quiz.length}
              <span className="text-lg ml-2">
                ({Math.round((calculateScore() / quizData.quiz.length) * 100)}%)
              </span>
            </p>
          </div>
        )}
        {reviewMode && (
          <div className="mt-4 bg-white text-gray-800 p-4 rounded-lg">
            <p className="text-lg font-semibold">
              📚 Review Mode - All correct answers are highlighted in green
            </p>
          </div>
        )}
      </div>

      <div className="space-y-4">
        {quizData.quiz.map((question, index) => (
          <div key={index} className="bg-white border border-gray-200 rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
            <div className="flex items-start justify-between mb-4">
              <h3 className="text-lg font-semibold text-gray-800 flex-1">
                <span className="text-blue-600 mr-2">Q{index + 1}.</span>
                {question.question}
              </h3>
              <span className={`ml-4 px-3 py-1 rounded-full text-xs font-semibold ${getDifficultyColor(question.difficulty)}`}>
                {question.difficulty}
              </span>
            </div>

            <div className="space-y-2 mb-4">
              {question.options.map((option, optIndex) => (
                <div
                  key={optIndex}
                  onClick={() => handleOptionSelect(index, option)}
                  className={`p-3 rounded-lg border transition-all ${getOptionClass(index, option, question.answer)}`}
                >
                  <span className="font-semibold mr-2">{String.fromCharCode(65 + optIndex)}.</span>
                  {option}
                  {showResults && option === question.answer && (
                    <span className="ml-2 text-green-600 font-semibold">✓ Correct</span>
                  )}
                  {showResults && userAnswers[index] === option && option !== question.answer && (
                    <span className="ml-2 text-red-600 font-semibold">✗ Wrong</span>
                  )}
                </div>
              ))}
            </div>

            {showResults && (
              <div className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
                <p className="text-sm font-semibold text-blue-900 mb-1">Explanation:</p>
                <p className="text-sm text-blue-800">{question.explanation}</p>
              </div>
            )}
          </div>
        ))}
      </div>

      <div className="flex gap-4 sticky bottom-4">
        {!showResults && !reviewMode ? (
          <button
            onClick={handleSubmit}
            className="flex-1 bg-gradient-to-r from-blue-500 to-purple-600 text-white px-6 py-3 rounded-lg font-semibold hover:from-blue-600 hover:to-purple-700 transition-all shadow-lg"
          >
            Submit Quiz ({Object.keys(userAnswers).length}/{quizData.quiz.length} answered)
          </button>
        ) : showResults && !reviewMode ? (
          <button
            onClick={handleRetake}
            className="flex-1 bg-gradient-to-r from-green-500 to-teal-600 text-white px-6 py-3 rounded-lg font-semibold hover:from-green-600 hover:to-teal-700 transition-all shadow-lg"
          >
            Retake Quiz
          </button>
        ) : null}
      </div>

      {quizData.related_topics && quizData.related_topics.length > 0 && (
        <div className="bg-purple-50 p-6 rounded-lg border border-purple-200">
          <h3 className="text-lg font-semibold text-purple-900 mb-3">Related Topics</h3>
          <div className="flex flex-wrap gap-2">
            {quizData.related_topics.map((topic, index) => (
              <span
                key={index}
                className="bg-purple-100 text-purple-800 px-3 py-1 rounded-full text-sm font-medium"
              >
                {topic}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default QuizDisplay;
