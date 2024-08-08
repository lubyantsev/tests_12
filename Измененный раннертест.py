import unittest
from runner import Runner
from functools import wraps


def skip_if_frozen(test_case):
    @wraps(test_case)
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
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


if __name__ == '__main__':
    unittest.main()
