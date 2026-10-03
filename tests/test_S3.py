import copy
import csv
import io
import unittest

import app

EXAMPLE = [{'title': 'Git', 'minutes': 30, 'done': False}, {'title': 'Python', 'minutes': 45, 'done': True}, {'title': 'Tests', 'minutes': 20, 'done': False}]


class TestS3(unittest.TestCase):
    def test_case_1(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.find_tasks(EXAMPLE, '  GIT '), [EXAMPLE[0]])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_2(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.find_tasks(EXAMPLE, '  '), EXAMPLE)
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_3(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.find_tasks(EXAMPLE, 'xyz'), [])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

    def test_case_4(self):
        original = copy.deepcopy(EXAMPLE)
        self.assertEqual(app.find_tasks([dict(title='Straße', minutes=5, done=False)], 'STRASSE'), [dict(title='Straße', minutes=5, done=False)])
        self.assertEqual(EXAMPLE, original, "Do not mutate input records")

