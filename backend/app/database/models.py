from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import os
from pathlib import Path

 
data_dir = Path(__file__).resolve().parents[2] / 'data'
os.makedirs(data_dir, exist_ok=True) 
db_path = os.path.join(data_dir, 'sqlite.db')

 
engine = create_engine(f"sqlite:///{db_path}", connect_args={"check_same_thread": False}) 

 
Base = declarative_base()

class ClassificationLog(Base):
    __tablename__ = "classification_logs"

    id = Column(Integer, primary_key=True, index=True)
    text_input = Column(String)   
    input_length = Column(Integer)
    predicted_label = Column(String, nullable=True)
    confidence = Column(Float, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    processing_time_ms = Column(Integer)
    client_ip = Column(String)
    status = Column(String)   
 
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print(f"Database initialized at: {db_path}")
