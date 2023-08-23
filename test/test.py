from rest_framework.test import APIClient

class TestAuthor:
    def test_anonymous_user_cannot_create_author(self):
        client = APIClient()
        client.post('')
