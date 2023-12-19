import unittest
from test_api_module1 import TestAPIModule1
from test_api_module2 import TestAPIModule2


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestAPIModule1))
    test_suite.addTest(unittest.makeSuite(TestAPIModule2))
    return test_suite
