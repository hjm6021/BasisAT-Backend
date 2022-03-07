from tabnanny import check
import unittest, sys, json

from flask import request

sys.path.append("..")
from start_app import app


class authTestCase(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
