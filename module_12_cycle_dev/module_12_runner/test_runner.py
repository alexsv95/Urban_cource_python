import unittest
import logging
from module_12_4 import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_test = Runner('runner_test', speed=-5)
            for _ in range(10):
                runner_test.walk()
            self.assertEqual(runner_test.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_test = Runner(1)
            for _ in range(10):
                runner_test.run()
            self.assertEqual(runner_test.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_test_1 = Runner('runner_test_1')
        runner_test_2= Runner('runner_test_2')
        for _ in range(10):
            runner_test_1.walk()
            runner_test_2.run()
        self.assertNotEqual(runner_test_1.distance, runner_test_2.distance)