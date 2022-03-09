import unittest, json
from start_app import app


class loginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.testing = True
        self.app = app.test_client()

    # Login Test - Case 1
    # Request to "/auth/login" with no data
    def test_Login_Case1(self):
        requestData = {}
        response = self.app.post(
            "/auth/login",
            data=json.dumps(requestData),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 400)

    # Login Test - Case 2
    # Request to "/auth/login" with username parameter only
    def test_Login_Case2(self):
        requestData = {"username": "admin"}
        response = self.app.post(
            "/auth/login",
            data=json.dumps(requestData),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 400)

    # Login Test - Case 3
    # Request to "/auth/login" with password parameter only
    def test_Login_Case3(self):
        requestData = {"password": "1234"}
        response = self.app.post(
            "/auth/login",
            data=json.dumps(requestData),
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(response.status_code, 400)
