import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

import pytest
from app import create_app

@pytest.fixture

def client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_interact_victor(client):
    response = client.post('/interact/victor', json={'input': 'Help me with my resume'})
    assert response.status_code == 200
    assert 'Victor says' in response.get_json()['response']
