TAHO Document Classifier
A document classification system using a machine learning model, accessible through a React-based user interface.

📁 Project Structure
graphql
Copier
Modifier
taho-document-classifier/
├── frontend/      # React app (TypeScript + TailwindCSS)
├── backend/       # FastAPI backend 
├── data/          # SQLite database 
├── tests/         # tests
⚙️ Installation & Execution
🔧 Backend Setup
bash
Copier
Modifier
# Navigate to backend folder
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows

# Install required packages
pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --reload

# to expose it to the local network on port 8000
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
🌐 Frontend Setup
bash
Copier
Modifier
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev