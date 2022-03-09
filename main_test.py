import unittest, sys, re

sys.path.append("..")
from tests.auth.test_login import loginTestCase

# Get all test cases which start with 'test_'
def getAllTestCases(testCase):
    testCaseNameExp = re.compile("test_*")
    attributes = dir(testCase)
    testCaseNames = list(filter(testCaseNameExp.match, attributes))

    allTestCases = list(testCase(testCaseName) for testCaseName in testCaseNames)

    return allTestCases


def suite():
    suite_set = unittest.TestSuite()

    # Authentication Unit Test
    # 1. /auth/login
    suite_set.addTests(getAllTestCases(loginTestCase))
    # 2. /auth/logout
    # 3. /auth/check

    return suite_set


if __name__ == "__main__":
    tests = suite()
    runner = unittest.TextTestRunner()
    runner.run(tests)
