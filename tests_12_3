import unittest
from runner import Runner
from runner_tournament import Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Атрибут для контроля заморозки тестов

    def test_walk(self):
        runner = Runner("бегун")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("бегун")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("бегун 1")
        runner2 = Runner("бегун 2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

    def _skip_if_frozen(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')

    def run(self, result=None):
        self._skip_if_frozen()
        super().run(result)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Атрибут для контроля заморозки тестов
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

    def _skip_if_frozen(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')

    def run(self, result=None):
        self._skip_if_frozen()
        super().run(result)

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results['Усэйн и Ник'] = results
        self.assertTrue(results[len(results)] == "Ник")

    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['Андрей и Ник'] = results
        self.assertTrue(results[len(results)] == "Ник")

    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results['Усэйн, Андрей и Ник'] = results
        self.assertTrue(results[len(results)] == "Ник")


if __name__ == '__main__':
    unittest.main()
