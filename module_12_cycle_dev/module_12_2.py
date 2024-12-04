import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, val in cls.all_result.items():
            print(val)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_result['tour_1'] = tour.start()
        result_tour = TournamentTest.all_result['tour_1']
        self.assertTrue(result_tour.get(2) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_result['tour_2'] = tour.start()
        result_tour = TournamentTest.all_result['tour_2']
        self.assertTrue(result_tour.get(2) == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_3(self):
        tour = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        TournamentTest.all_result['tour_3'] = tour.start()
        result_tour = TournamentTest.all_result['tour_3']
        self.assertTrue(result_tour.get(3) == 'Ник')


if __name__ == '__main__':
    unittest.main()



