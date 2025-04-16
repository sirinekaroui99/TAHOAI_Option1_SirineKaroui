import axios from 'axios';
import { ClassificationResponse } from '../interfaces/types';

const API_URL = 'http://localhost:8000';

export const classifyDocument = async (text: string): Promise<ClassificationResponse> => {
  try {
    const response = await axios.post(`${API_URL}/classify`, { text });
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      throw new Error(error.response.data.detail || 'Une erreur est survenue lors de la classification');
    }
    throw new Error('Impossible de se connecter au serveur');
  }
};