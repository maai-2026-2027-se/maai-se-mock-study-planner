import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Git', 'minutes': 30, 'done': False}, {'title': 'Python', 'minutes': 45, 'done': True}, {'title': 'Tests', 'minutes': 20, 'done': False}]


class TestS4(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        original = copy.deepcopy(EXAMPLE)
        result = app.mark_done(original, 'Git')
        self.assertTrue(result[0]['done'])
        self.assertEqual(original, EXAMPLE)
        for before, after in zip(original, result):
            self.assertIsNot(before, after)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        with self.assertRaises(KeyError):
            app.mark_done(EXAMPLE, 'missing')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.mark_done([EXAMPLE[1]], 'Python'), [EXAMPLE[1]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_4(self):
        original = copy.deepcopy(EXAMPLE)
        rows = [dict(title='x', minutes=2, done=False), dict(title='x', minutes=3, done=False)]
        self.assertTrue(all(row['done'] for row in app.mark_done(rows, 'x')))
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

