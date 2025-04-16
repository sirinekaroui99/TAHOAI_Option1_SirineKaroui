from typing import Tuple
import re
import random
 
DOCUMENT_TYPES = {
    "Invoice": [
        "invoice", "bill", "payment", "amount", "due", "total", "tax", "qty", "quantity", 
        "price", "purchase", "order", "account", "customer", "vendor", "paid"
    ],
    "Contract": [
        "agreement", "contract", "terms", "conditions", "parties", "clause", "hereby", "shall", 
        "undersigned", "obligations", "rights", "signature", "execute", "legal", "binding"
    ],
    "Resume": [
        "resume", "cv", "curriculum", "vitae", "experience", "skills", "education", "work", 
        "employment", "job", "career", "objective", "professional", "references", "qualifications"
    ],
    "Email": [
        "from:", "to:", "subject:", "cc:", "bcc:", "forwarded", "replied", "sent", "received", 
        "attachment", "regards", "sincerely", "hello", "hi", "dear"
    ] 
}

def classify_text(text: str) -> Tuple[str, float]:
 
    text = text.lower()
     
    scores = {}
    for doc_type, keywords in DOCUMENT_TYPES.items():
        matches = 0
        for keyword in keywords:
             
            pattern = r'\b' + re.escape(keyword) + r'\b'
            matches += len(re.findall(pattern, text))
            print("print matches",matches) 
        if matches > 0:
            scores[doc_type] = matches / len(keywords)
     
    if not scores:
        return "Unknown", 0.2
     
    best_type = max(scores.items(), key=lambda x: x[1])
    doc_type, score = best_type
      
    base_confidence = min(0.5 + (score * 0.5), 0.98)   
    confidence = base_confidence + (random.random() * 0.04 - 0.02)  
    
    return doc_type, round(confidence, 2)
  