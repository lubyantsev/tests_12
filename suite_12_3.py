import unittest
from runner import Runner
from runner_tournament import Tournament
from your_test_module import RunnerTest, TournamentTest  # Замените your_test_module на название файла с вашими тестами

# Создаем объект TestSuite
test_suite = unittest.TestSuite()

# Добавляем тесты RunnerTest и TournamentTest в TestSuite
test_suite.addTest(unittest.makeSuite(RunnerTest))
test_suite.addTest(unittest.makeSuite(TournamentTest))

# Создаем объект класса TextTestRunner с verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем тесты
if __name__ == '__main__':
    runner.run(test_suite)
