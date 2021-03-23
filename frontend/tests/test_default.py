import json
import requests
import pytest


# custom class to be the mock return value of requests.get()
class MockResponse:
    @staticmethod
    def json():
        return {
            'status': 'success',
            'message': '',
            'data': [
                {
                    'email': 'user1@example.com',
                    'username': 'user1',
                    'active': True
                },
                {
                    'email': 'user2@example.com',
                    'username': 'user2',
                    'active': False
                }
            ]}
    
    @staticmethod
    def raise_for_status():
        return True


# monkeypatched requests.get moved to a fixture
@pytest.fixture
def mock_response(monkeypatch):
    """Requests.get() mocked."""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

# def test_default_route(client, mock_response):
#     response = client.get('/users')
#     # response = json.loads(response['data'])

#     assert 'status' in response.json
#     assert response.json['status'] == 'success'
