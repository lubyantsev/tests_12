import logging
import unittest

# Настройка логирования
logging.basicConfig(
    filename='runner_tests.log',
    level=logging.INFO,
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Baca', -5)  # Передаем отрицательное значение в speed
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            logging.exception(e)

    def test_run(self):
        try:
            runner = Runner(2)  # Передаем неверный тип (не строка) в name
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.exception(e)

if __name__ == '__main__':
    unittest.main()
