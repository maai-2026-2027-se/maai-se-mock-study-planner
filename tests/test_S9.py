import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Git', 'minutes': 30, 'done': False}, {'title': 'Python', 'minutes': 45, 'done': True}, {'title': 'Tests', 'minutes': 20, 'done': False}]


class TestS9(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.to_csv([]), 'title,minutes,done\n')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.to_csv(EXAMPLE), 'title,minutes,done\nGit,30,0\nPython,45,1\nTests,20,0\n')
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        rows = [dict(title='A, \"B\"\nC', minutes=1, done=True)]
        self.assertEqual(list(csv.reader(io.StringIO(app.to_csv(rows)))), [['title', 'minutes', 'done'], ['A, \"B\"\nC', '1', '1']])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

