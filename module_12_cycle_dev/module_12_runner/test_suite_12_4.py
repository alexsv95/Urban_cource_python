import unittest
from test_runner import RunnerTest

def get_suite():
    suite = unittest.TestSuite()
    load_test = unittest.TestLoader().loadTestsFromTestCase(RunnerTest)
    suite.addTest(load_test)
    return suite
