import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users(client):
    """Test the /api/users endpoint"""
    rv = client.get('/api/users')
    assert rv.status_code == 200

def test_add_user(client):
    """Test the /api/users endpoint"""
    rv = client.post('/api/users', json={
        "name": "test",
        "job": "test",
        "email": "test@test.com"
    })
    assert rv.status_code == 200
