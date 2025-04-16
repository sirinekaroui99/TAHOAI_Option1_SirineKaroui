from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.database.models import Base, engine
 
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TAHO Document Classifier API")
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "TAHO Document Classifier API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)