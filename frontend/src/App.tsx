 
import ClassifierPage from './pages/ClassifierPage';
import './index.css';


function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-indigo-600 shadow">
        <div className="max-w-7xl mx-auto py-4 px-4">
          <h1 className="text-2xl font-bold text-white">TAHO AI - Document Classifier</h1>
        </div>
      </header>
      <main>
        <ClassifierPage />
      </main>
    </div>
  );
}

export default App;