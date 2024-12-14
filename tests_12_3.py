import unittest  # Импортируем модуль unittest, который предоставляет инструменты для написания и выполнения тестов

# Определяем класс RunnerTest, который наследует от unittest.TestCase
class RunnerTest(unittest.TestCase):
    is_frozen = False  # Устанавливаем атрибут is_frozen в False, что позволяет выполнять тесты

    def test_challenge(self):
        # Тест, проверяющий, что 1 + 1 равно 2
        self.assertEqual(1 + 1, 2)

    def test_run(self):
        # Тест, проверяющий, что выражение True является истинным
        self.assertTrue(True)

    def test_walk(self):
        # Тест, проверяющий, что выражение False является ложным
        self.assertFalse(False)

# Определяем класс TournamentTest, который наследует от unittest.TestCase
class TournamentTest(unittest.TestCase):
    is_frozen = True  # Устанавливаем атрибут is_frozen в True, что приводит к пропуску тестов

    def test_first_tournament(self):
        # Тест, проверяющий, что 2 * 2 равно 4
        self.assertEqual(2 * 2, 4)

    def test_second_tournament(self):
        # Тест, проверяющий, что выражение False является ложным
        self.assertTrue(False)

    def test_third_tournament(self):
        # Тест, проверяющий, что число 1 содержится в списке [1, 2, 3]
        self.assertIn(1, [1, 2, 3])