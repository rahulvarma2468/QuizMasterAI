import React from 'react';

const QuizDisplay = ({ quizData }) => {
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

  return (
    <div className="space-y-6">
      <div className="bg-gradient-to-r from-blue-500 to-purple-600 text-white p-6 rounded-lg shadow-lg">
        <h2 className="text-3xl font-bold mb-2">{quizData.title}</h2>
        <p className="text-blue-100">{quizData.summary}</p>
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
                  className={`p-3 rounded-lg border ${
                    option === question.answer
                      ? 'bg-green-50 border-green-300 font-medium'
                      : 'bg-gray-50 border-gray-200'
                  }`}
                >
                  <span className="font-semibold mr-2">{String.fromCharCode(65 + optIndex)}.</span>
                  {option}
                  {option === question.answer && (
                    <span className="ml-2 text-green-600 font-semibold">✓ Correct</span>
                  )}
                </div>
              ))}
            </div>

            <div className="bg-blue-50 border-l-4 border-blue-500 p-4 rounded">
              <p className="text-sm font-semibold text-blue-900 mb-1">Explanation:</p>
              <p className="text-sm text-blue-800">{question.explanation}</p>
            </div>
          </div>
        ))}
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
