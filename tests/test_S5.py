import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Git', 'minutes': 30, 'done': False}, {'title': 'Python', 'minutes': 45, 'done': True}, {'title': 'Tests', 'minutes': 20, 'done': False}]


class TestS5(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.estimate_sessions(51, 25), 3)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.estimate_sessions(50, 25), 2)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.estimate_sessions(0, 25), 0)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_4(self):
        original = copy.deepcopy(EXAMPLE)
        for minutes, block in [(-1, 25), (10, 0), (10, -2)]:
            with self.subTest(minutes=minutes, block=block), self.assertRaises(ValueError):
                app.estimate_sessions(minutes, block)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

