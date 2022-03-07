import unittest, sys

sys.path.append("..")
from tests.test_auth import authTestCase


def suite():
    suite_set = unittest.TestSuite()
    suite_set.addTest(authTestCase("test_Login_Case1"))
    return suite_set


if __name__ == "__main__":
    tests = suite()
    runner = unittest.TextTestRunner()
    runner.run(tests)
