import unittest

from unittest import TestCase
from main_task1 import solve, vote, max_min_course, mentors, courses


class TestMain(TestCase):
    #тест функции solve из задания "Кто быстрее"
    def test_solve_with_params(self):
        for i, (a, b, expected) in enumerate([
            ([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3], 'черепаха'),
            ([8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3], 'заяц'),
            ([8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3], 'одинаково'),
        ]):
            with self.subTest(i):
                result = solve(a, b)
                self.assertEqual(expected, result)

    # тест функции vote из задания "Голосование"
    def test_vote_with_params(self):
        for i, (a, expected) in enumerate([
            ([1, 1, 1, 2, 3], 1),
            ([1, 2, 3, 2, 2], 2),
        ]):
            with self.subTest(i):
                result = vote(a)
                self.assertEqual(expected, result)

    # тест функции max_min_course из задания "«Рекордсмены: находим самый продолжительный и самый короткий курс по программированию»"
    def test_max_min_course_with_params(self):
        for i, (a, b, x, expected) in enumerate([
            (courses, mentors, [14, 20, 12, 20],
             ('Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)',
              'Самый длинный курс(ы): Fullstack-разработчик на Python, '
              'Frontend-разработчик с нуля - 20 месяца(ев)')
             ),

            (courses, mentors, [14, 13, 12, 5],
             ('Самый короткий курс(ы): Frontend-разработчик с нуля - 5 месяца(ев)',
              'Самый длинный курс(ы): Java-разработчик с нуля - 14 месяца(ев)')
             )
        ]):
            with self.subTest(i):
                result = max_min_course(a, b, x)
                self.assertEqual(expected, result)
