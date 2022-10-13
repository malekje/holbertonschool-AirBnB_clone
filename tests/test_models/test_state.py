#!/usr/bin/python3
"""unittest State"""

from models.state import State
import unittest
import uuid


class Test_User(unittest.TestCase):
    """Test Class State"""
     
    def test_name_is_public_str(self):
        self.assertEqual(str, type(State.name))
