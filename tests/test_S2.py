import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Git', 'minutes': 30, 'done': False}, {'title': 'Python', 'minutes': 45, 'done': True}, {'title': 'Tests', 'minutes': 20, 'done': False}]


class TestS2(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.completion_rate(EXAMPLE), 33.3)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.completion_rate([]), 0.0)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.completion_rate([EXAMPLE[1]]), 100.0)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

