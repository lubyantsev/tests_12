import logging
import unittest

# Настройка логирования
logging.basicConfig(
    filename='runner_tests.log',
    level=logging.INFO,
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Baca', -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            logging.exception(e)

    def test_run(self):
        try:
            runner = Runner(2)  # Передаем неверный тип (не строка)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.exception(e)


if __name__ == '__main__':
    unittest.main()
