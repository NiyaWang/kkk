import logging
import unittest
import rt_with_exceptions as rt



class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    def test_walk(self):
        try:
            r1 = rt.Runner('Name', -10)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
        except ValueError:
            logging.error('Ошибка', exc_info=True)
            logging.warning("Неверная скорость для Runner")
        logging.info('"test_walk" выполнен успешно')


    def test_run(self):
        try:
            r2 = rt.Runner(19,15)
            for i in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
        except TypeError:
            logging.error('Ошибка', exc_info=True)
            logging.warning("Неверный тип данных для объекта Runner")
        logging.info('"test_run" выполнен успешно')


if __name__ == "__main__":
    unittest.main()
