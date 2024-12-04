from module_12_1 import RunnerTest
from module_12_2 import TournamentTest
import unittest

runner_suite = unittest.TestSuite()

runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
runner_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

unittest.TextTestRunner(verbosity=2).run(runner_suite)