import React, { useState } from 'react';
import DocumentInput from '../components/DocumentInput';
import ClassificationResult from '../components/ClassificationResult';
import LoadingIndicator from '../components/LoadingIndicator';
import ErrorMessage from '../components/ErrorMessage';
import { classifyDocument } from '../services/api';
import { ClassificationResponse, LoadingState } from '../interfaces/types';

const ClassifierPage: React.FC = () => {
  const [result, setResult] = useState<ClassificationResponse | null>(null);
  const [loadingState, setLoadingState] = useState<LoadingState>(LoadingState.IDLE);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const handleSubmit = async (text: string) => {
    setLoadingState(LoadingState.LOADING);
    setErrorMessage(null);

    try {
      const response = await classifyDocument(text);
      setResult(response);
      setLoadingState(LoadingState.SUCCESS);
    } catch (error) {
      console.error('Error classifying document:', error);
      setErrorMessage(error instanceof Error ? error.message : 'An unknown error occurred');
      setLoadingState(LoadingState.ERROR);
    }
  };

  const clearError = () => {
    setErrorMessage(null);
  };

  return (
    <div className="max-w-3xl mx-auto py-8 px-4">
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Document Classifier</h1>
        <p className="mt-2 text-gray-600">Paste your text or upload a file to classify the document type</p>
      </div>

      <DocumentInput onTextSubmit={handleSubmit} isLoading={loadingState === LoadingState.LOADING} />

      <LoadingIndicator isLoading={loadingState === LoadingState.LOADING} />

      <ErrorMessage message={errorMessage} onDismiss={clearError} />

      {loadingState === LoadingState.SUCCESS && (
        <ClassificationResult result={result} />
      )}
    </div>
  );
};

export default ClassifierPage;
