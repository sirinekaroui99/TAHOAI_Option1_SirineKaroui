from sqlalchemy.orm import Session
from app.database.models import engine, ClassificationLog
from typing import Optional

def get_db():
     
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

def log_classification(
    text_input: str,
    input_length: int,
    predicted_label: Optional[str],
    confidence: Optional[float],
    processing_time_ms: int,
    client_ip: str,
    status: str
):
     
    db = Session(engine)
    try:
        log_entry = ClassificationLog(
            text_input=text_input,
            input_length=input_length,
            predicted_label=predicted_label,
            confidence=confidence,
            processing_time_ms=processing_time_ms,
            client_ip=client_ip,
            status=status
        )
        db.add(log_entry)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error logging classification: {e}")
    finally:
        db.close()

def get_classification_history(skip: int = 0, limit: int = 100):
 
    db = Session(engine)
    try:
        return db.query(ClassificationLog).order_by(
            ClassificationLog.timestamp.desc()
        ).offset(skip).limit(limit).all()
    finally:
        db.close()