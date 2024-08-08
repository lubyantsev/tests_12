import unittest
from runner_tournament import Runner, Tournament
from functools import wraps

def skip_if_frozen(test_case):
    @wraps(test_case)
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return test_case(self, *args, **kwargs)
    return wrapper

class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True  # Атрибут для заморозки тестов

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @skip_if_frozen
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results['Усэйн и Ник'] = results
        self.assertTrue(results[len(results)] == "Ник")

    @skip_if_frozen
    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['Андрей и Ник'] = results
        self.assertTrue(results[len(results)] == "Ник")

    @skip_if_frozen
    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['Усэйн, Андрей и Ник'] = results
        self.assertTrue(results[len(results)] == "Ник")


if __name__ == '__main__':
    unittest.main()
