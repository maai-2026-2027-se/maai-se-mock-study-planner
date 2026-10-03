import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Git', 'minutes': 30, 'done': False}, {'title': 'Python', 'minutes': 45, 'done': True}, {'title': 'Tests', 'minutes': 20, 'done': False}]


class TestS8(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.statistics(EXAMPLE), {'total_minutes': 95, 'pending_minutes': 50, 'completion_percent': 33.3})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.statistics([]), {'total_minutes': 0, 'pending_minutes': 0, 'completion_percent': 0.0})
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

