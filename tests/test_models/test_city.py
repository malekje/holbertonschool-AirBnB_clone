#!/usr/bin/python3
"""unittest City Class"""

from models.city import City
import uuid
import unittest

class Test_User(unittest.TestCase):
    """ Test class City """
    def test_state_id(self):
        self.assertEqual(str, type(City.state_id))

    def test_name(self):
        self.assertEqual(str, type(City.name))
