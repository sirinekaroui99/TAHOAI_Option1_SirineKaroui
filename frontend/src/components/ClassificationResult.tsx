import React from 'react';
import { ClassificationResponse } from '../interfaces/types';

interface ClassificationResultProps {
  result: ClassificationResponse | null;
}

const ClassificationResult: React.FC<ClassificationResultProps> = ({ result }) => {
  if (!result) return null;

  const getConfidenceColorClass = (confidence: number): string => {
    if (confidence >= 0.8) return 'text-green-700';
    if (confidence >= 0.6) return 'text-yellow-600';
    return 'text-red-600';
  };

  const confidencePercentage = Math.round(result.confidence * 100);
  const confidenceColor = getConfidenceColorClass(result.confidence);

  return (
    <div className="bg-white p-6 rounded-lg shadow-md mt-4">
      <h2 className="text-lg font-medium text-gray-900 mb-4">Classification Result</h2>
      
      <div className="flex flex-col space-y-3">
        <div>
          <span className="text-sm text-gray-500">Document type:</span>
          <div className="text-xl font-semibold mt-1">{result.label}</div>
        </div>
        
        <div>
          <span className="text-sm text-gray-500">Confidence level:</span>
          <div className={`text-xl font-semibold mt-1 ${confidenceColor}`}>
            {confidencePercentage}%
          </div>
          
          <div className="w-full bg-gray-200 rounded-full h-2.5 mt-2">
            <div 
              className={`h-2.5 rounded-full ${result.confidence >= 0.8 ? 'bg-green-600' : result.confidence >= 0.6 ? 'bg-yellow-500' : 'bg-red-500'}`}
              style={{ width: `${confidencePercentage}%` }}
            ></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ClassificationResult;
