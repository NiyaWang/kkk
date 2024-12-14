import unittest  # Импортируем модуль unittest для работы с тестами
from tests_12_3 import RunnerTest, TournamentTest  # Импортируем классы тестов из модуля tests_12_3

# Декоратор для пропуска тестов, если is_frozen равно True
def skip_if_frozen(test_method):
    # Определяем обертку для метода теста
    def wrapper(self):
        # Проверяем значение атрибута is_frozen у текущего тестового класса
        if getattr(self, 'is_frozen', False):
            # Если is_frozen равно True, пропускаем тест и выводим сообщение
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        # Если is_frozen равно False, выполняем тест
        return test_method(self)
    return wrapper  # Возвращаем обернутый метод

# Обновляем класс RunnerTest с декораторами для методов тестов
class RunnerTest(unittest.TestCase):
    is_frozen = False  # Устанавливаем атрибут is_frozen в False

    @skip_if_frozen  # Применяем декоратор к методу теста
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)  # Проверка, что 1 + 1 равно 2

    @skip_if_frozen  # Применяем декоратор к методу теста
    def test_run(self):
        self.assertTrue(True)  # Проверка, что выражение True является истинным

    @skip_if_frozen  # Применяем декоратор к методу теста
    def test_walk(self):
        self.assertFalse(False)  # Проверка, что выражение False является ложным

# Обновляем класс TournamentTest с декораторами для методов тестов
class TournamentTest(unittest.TestCase):
    is_frozen = True  # Устанавливаем атрибут is_frozen в True

    @skip_if_frozen  # Применяем декоратор к методу теста
    def test_first_tournament(self):
        self.assertEqual(2 * 2, 4)  # Проверка, что 2 * 2 равно 4

    @skip_if_frozen  # Применяем декоратор к методу теста
    def test_second_tournament(self):
        self.assertTrue(False)  # Проверка, что выражение False является ложным

    @skip_if_frozen  # Применяем декоратор к методу теста
    def test_third_tournament(self):
        self.assertIn(1, [1, 2, 3])  # Проверка, что число 1 содержится в списке [1, 2, 3]

# Функция для создания тестового набора
def suite():
    test_suite = unittest.TestSuite()  # Создаем новый объект тестового набора
    test_suite.addTest(unittest.makeSuite(RunnerTest))  # Добавляем тесты из RunnerTest в тестовый набор
    test_suite.addTest(unittest.makeSuite(TournamentTest))  # Добавляем тесты из TournamentTest в тестовый набор
    return test_suite  # Возвращаем созданный тестовый набор

# Проверяем, запущен ли файл как основной модуль
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)  # Создаем объект тестового запуска с подробным выводом
    runner.run(suite())  # Запускаем тесты из созданного тестового набора