import json
import requests
import pytest


# custom class to be the mock return value of requests.post()
class MockResponse:
    @staticmethod
    def json():
        return {
            'status': 'success',
            'message': 'User was added!',
            'data': {
                'email': 'user1@example.com',
                'username': 'user1',
                'active': True
            }
        }
    
    @staticmethod
    def raise_for_status():
        return True


# monkeypatched requests.get moved to a fixture
@pytest.fixture
def mock_response(monkeypatch):
    """Requests.post()."""

    def mock_post(*args, **kwargs):
        return MockResponse()

    
    monkeypatch.setattr(requests, "post", mock_post)


# class TestAuthBlueprint(object):

#     def test_user_registration(self, client, mock_response):
#         response = client.post(
#             '/user',
#             data=json.dumps({
#                 'username': 'user1',
#                 'email': 'user1@example.com',
#                 'password': 'password',
#             }),
#             content_type='application/json'
#         )
#         assert response.json['data']['status'] == 'success'
#         # data = json.loads(response.data.decode())
#         # assert data['status'] == 'success'
#         # assert data['message'] == 'Successfully registered.'
#         # assert data['auth_token']
#         # assert response.content_type == 'application/json'
#         # assert response.status_code == 201
