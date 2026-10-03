import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Git', 'minutes': 30, 'done': False}, {'title': 'Python', 'minutes': 45, 'done': True}, {'title': 'Tests', 'minutes': 20, 'done': False}]


class TestS7(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.daily_plan(EXAMPLE, 50), [EXAMPLE[0], EXAMPLE[2]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.daily_plan(EXAMPLE, 20), [EXAMPLE[2]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        zero = dict(title='zero', minutes=0, done=False)
        self.assertEqual(app.daily_plan([zero] + EXAMPLE, 0), [zero])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_4(self):
        original = copy.deepcopy(EXAMPLE)
        with self.assertRaises(ValueError):
            app.daily_plan([], -1)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

