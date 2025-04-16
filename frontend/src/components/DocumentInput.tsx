import React, { useState, ChangeEvent } from 'react';
import pdfToText from 'react-pdftotext';

interface DocumentInputProps {
  onTextSubmit: (text: string) => void;
  isLoading: boolean;
}

const DocumentInput: React.FC<DocumentInputProps> = ({ onTextSubmit, isLoading }) => {
  const [text, setText] = useState<string>('');
  const [fileName, setFileName] = useState<string>('');

  const handleTextChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    setText(e.target.value);
  };

  function extractText(event: React.ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0];
    if (!file) return;

    setFileName(file.name);

    pdfToText(file)
      .then((extractedText) => {
        setText(extractedText);
      })
      .catch((error) => {
        console.error("Failed to extract text from PDF:", error);
      });
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (text.trim()) {
      onTextSubmit(text);
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label htmlFor="document-text" className="block text-sm font-medium text-gray-700 mb-1">
            Document text
          </label>
          <textarea
            id="document-text"
            className="w-full h-64 p-3 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
            placeholder="Paste the document text here..."
            value={text}
            onChange={handleTextChange}
            disabled={isLoading}
          />
        </div>

        <div className="flex items-center justify-between">
          <div className="relative">
            <label 
              htmlFor="document-file" 
              className="cursor-pointer bg-white py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 hover:bg-gray-50"
            >
              Upload a file
            </label>
            <input
              id="document-file"
              type="file"
              className="hidden"
              disabled={isLoading}
              accept="application/pdf"
              onChange={extractText}
            />
            {fileName && (
              <span className="ml-3 text-sm text-gray-500">{fileName}</span>
            )}
          </div>

          <button
            type="submit"
            className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
            disabled={isLoading || !text.trim()}
          >
            Classify
          </button>
        </div>
      </form>
    </div>
  );
};

export default DocumentInput;
