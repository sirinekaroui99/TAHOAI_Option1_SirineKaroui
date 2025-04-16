from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
import time
from typing import Optional
from app.models.classifier import classify_text
from app.database.operations import log_classification
from app.utils.validators import validate_text_input

router = APIRouter()

class ClassificationRequest(BaseModel):
    text: str

class ClassificationResponse(BaseModel):
    label: str
    confidence: float

@router.post("/classify", response_model=ClassificationResponse)
async def classify_document(
    request: Request,
    classification_request: ClassificationRequest
):
    
    text = classification_request.text
    print('text',text)
    if error := validate_text_input(text):
        raise HTTPException(status_code=400, detail=error)
    
     
    start_time = time.time()
    
    try:
        
        label, confidence = classify_text(text)
        
         
        processing_time = int((time.time() - start_time) * 1000)
        
         
        client_ip = request.client.host if request.client else "unknown"
        log_classification(
            text_input=text[:500],   
            input_length=len(text),
            predicted_label=label,
            confidence=confidence,
            processing_time_ms=processing_time,
            client_ip=client_ip,
            status="success"
        )
        
        return ClassificationResponse(label=label, confidence=confidence)
    
    except Exception as e: 
        processing_time = int((time.time() - start_time) * 1000)
        client_ip = request.client.host if request.client else "unknown"
        log_classification(
            text_input=text[:500],
            input_length=len(text),
            predicted_label=None,
            confidence=None,
            processing_time_ms=processing_time,
            client_ip=client_ip,
            status=f"error: {str(e)}"
        )
        
        raise HTTPException(status_code=500, detail=f"Classification error: {str(e)}")

 