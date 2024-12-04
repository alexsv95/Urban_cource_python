import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_test = Runner('runner_test')
        for _ in range(10):
            runner_test.walk()
        self.assertEqual(runner_test.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_test = Runner('runner_test')
        for _ in range(10):
            runner_test.run()
        self.assertEqual(runner_test.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_test_1 = Runner('runner_test_1')
        runner_test_2= Runner('runner_test_2')
        for _ in range(10):
            runner_test_1.walk()
            runner_test_2.run()
        self.assertNotEqual(runner_test_1.distance, runner_test_2.distance)


if __name__ == '__main__':
    unittest.main()
