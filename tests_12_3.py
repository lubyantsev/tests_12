import unittest
from runner import Runner
from runner_tournament import Runner, Tournament
from functools import wraps


def skip_if_frozen(test_case):
    @wraps(test_case)
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print("Тесты в этом кейсе заморожены")
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return test_case(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут для RunnerTest

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("бегун")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("бегун")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("бегун 1")
        runner2 = Runner("бегун 2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Атрибут для TournamentTest
    all_results = {}

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
