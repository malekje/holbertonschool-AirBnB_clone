#!/usr/bin/python3
"""unittest class Reviw"""



from models.review import Review
import uuid
import unittest


class Test_User(unittest.TestCase):
    """Class Test Review"""
    def test_place_id(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text(self):
        self.assertEqual(str, type(Review.text))
