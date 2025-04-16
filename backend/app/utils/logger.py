import logging
import sys
from pathlib import Path
 
log_dir = Path(__file__).resolve().parents[2] / 'logs'
log_dir.mkdir(exist_ok=True)
 
def setup_logger():
    logger = logging.getLogger("taho_classifier")
    logger.setLevel(logging.INFO)
     
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_format)
     
    file_handler = logging.FileHandler(log_dir / "classifier.log")
    file_handler.setLevel(logging.INFO)
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)
     
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger
 
logger = setup_logger()