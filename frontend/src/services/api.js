import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export const generateQuiz = async (url) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/generate_quiz`, { url });
    return response.data;
  } catch (error) {
    throw error.response?.data?.detail || 'Failed to generate quiz';
  }
};

export const getHistory = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/history`);
    return response.data;
  } catch (error) {
    throw error.response?.data?.detail || 'Failed to fetch history';
  }
};

export const getQuiz = async (quizId) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/quiz/${quizId}`);
    return response.data;
  } catch (error) {
    throw error.response?.data?.detail || 'Failed to fetch quiz';
  }
};
