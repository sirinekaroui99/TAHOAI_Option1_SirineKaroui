import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_classify_valid_invoice():
     
    invoice_text = """
    INVOICE #12345
    Date: 2023-04-15
    
    Bill To:
    ACME Corporation
    123 Main St
    Anytown, USA
    
    Item     Qty    Price    Total
    Widget A  2     $10.00   $20.00
    Widget B  3     $15.00   $45.00
    
    Subtotal: $65.00
    Tax (10%): $6.50
    Total Due: $71.50
    
    Payment due within 30 days.
    """
    
    response = client.post("/classify", json={"text": invoice_text})
    assert response.status_code == 200
    result = response.json()
    assert result["label"] == "Invoice"
    assert isinstance(result["confidence"], float)
    assert 0 <= result["confidence"] <= 1

def test_classify_empty_text():
    response = client.post("/classify", json={"text": ""})
    assert response.status_code == 400
    assert "vide" in response.json()["detail"].lower()

def test_classify_short_text():
    response = client.post("/classify", json={"text": "Hi there"})
    assert response.status_code == 400
    assert "court" in response.json()["detail"].lower()