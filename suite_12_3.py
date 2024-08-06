import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создание объекта TestSuite
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))

# Создание объекта TextTestRunner и запуск тестов
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
