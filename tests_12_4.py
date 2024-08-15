import unittest
import logging
from runner import Runner
from functools import wraps


logging.basicConfig(
    filename='runner_tests.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


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
        try:
            runner = Runner("бегун", -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(runner.distance, 0)
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    @skip_if_frozen
    def test_run(self):
        try:
            runner = Runner(12345)
            runner.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(runner.distance, 0)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("бегун 1")
        runner2 = Runner("бегун 2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
