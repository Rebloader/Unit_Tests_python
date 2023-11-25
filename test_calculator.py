import unittest

from main import Calculator


class MyTest(unittest.TestCase):

    def test_compare_averages_1(self):
        calculator = Calculator([5, 7, 9], [3, 10, 2])
        self.assertEqual(calculator.compare_average(), 'Первый список имеет большее среднее значение')

    def test_compare_averages_2(self):

        calculator = Calculator([1, 4, 2], [3, 10, 2])
        self.assertEqual(calculator.compare_average(), 'Второй список имеет большее среднее значение')

    def test_compare_average_equals(self):

        calculator = Calculator([1, 2, 3], [3, 2, 1])
        self.assertEqual(calculator.compare_average(), 'Средние значения равны')

    def test_compare_average_empty(self):

        calculator = Calculator([], [])
        self.assertEqual(calculator.compare_average(), 'Средние значения равны')
