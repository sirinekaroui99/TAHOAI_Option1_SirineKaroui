import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import DocumentInput from '../../../frontend/src/components/DocumentInput';

test('renders textarea and buttons', () => {
  const mockSubmit = jest.fn();
  render(<DocumentInput onTextSubmit={mockSubmit} isLoading={false} />);
   
  expect(screen.getByLabelText(/texte du document/i)).toBeInTheDocument();
  expect(screen.getByText(/importer un fichier/i)).toBeInTheDocument();
  expect(screen.getByText(/classifier/i)).toBeInTheDocument();
});

test('submit button is disabled when text is empty', () => {
  const mockSubmit = jest.fn();
  render(<DocumentInput onTextSubmit={mockSubmit} isLoading={false} />);
  
  const submitButton = screen.getByText(/classifier/i);
  expect(submitButton).toBeDisabled();
});

test('can enter text and submit', () => {
  const mockSubmit = jest.fn();
  render(<DocumentInput onTextSubmit={mockSubmit} isLoading={false} />);
  
 
  const textarea = screen.getByLabelText(/texte du document/i);
  fireEvent.change(textarea, { target: { value: 'Sample text for classification' } });
  
 
  const submitButton = screen.getByText(/classifier/i);
  expect(submitButton).not.toBeDisabled();
  fireEvent.click(submitButton);
   
  expect(mockSubmit).toHaveBeenCalledWith('Sample text for classification');
});

test('form is disabled when loading', () => {
  const mockSubmit = jest.fn();
  render(<DocumentInput onTextSubmit={mockSubmit} isLoading={true} />);
 
  expect(screen.getByLabelText(/texte du document/i)).toBeDisabled();
  expect(screen.getByText(/classifier/i)).toBeDisabled();
});