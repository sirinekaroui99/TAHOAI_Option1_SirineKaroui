from typing import Optional

def validate_text_input(text: str) -> Optional[str]:
 
    if not text:
        return "Le texte du document ne peut pas être vide"
    
    if len(text) < 10:
        return "Le texte est trop court pour être classifié (minimum 10 caractères)"
    
    if len(text) > 100000:
        return "Le texte est trop long (maximum 100 000 caractères)"
    
    return None