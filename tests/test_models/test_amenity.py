#!/usr/bin/python3
"""unittest Amenity Class"""



from models.amenity import Amenity
import uuid
import unittest


class Test_User(unittest.TestCase):
    """Amenity Test"""
    def test_name_is_public_str(self):
        self.assertEqual(str, type(Amenity.name))
