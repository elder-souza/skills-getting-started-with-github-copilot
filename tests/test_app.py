import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# AAA: Arrange-Act-Assert

def test_root_endpoint():
    # Arrange
    # (Nada a preparar para GET /)
    
    # Act
    response = client.get("/")
    
    # Assert
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.text
    assert "<html" in response.text
    assert "<head>" in response.text
    assert "<body" in response.text

# Adicione outros testes AAA conforme necessário
