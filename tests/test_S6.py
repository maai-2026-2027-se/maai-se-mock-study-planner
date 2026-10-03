import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Git', 'minutes': 30, 'done': False}, {'title': 'Python', 'minutes': 45, 'done': True}, {'title': 'Tests', 'minutes': 20, 'done': False}]


class TestS6(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.sort_tasks(EXAMPLE), [EXAMPLE[1], EXAMPLE[0], EXAMPLE[2]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        rows = [dict(title=t, minutes=10, done=False) for t in ['z', 'A', 'a']]
        self.assertEqual(app.sort_tasks(rows), [rows[1], rows[2], rows[0]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        rows = copy.deepcopy(EXAMPLE)
        app.sort_tasks(rows)
        self.assertEqual(rows, EXAMPLE)
        self.assertEqual(app.sort_tasks([]), [])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

