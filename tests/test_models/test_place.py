#!/usr/bin/python3
"""unittest Class Place"""




from models.place import Place
import uuid
import unittest


class Test_Place(unittest.TestCase):
    """Class Test Place"""
    def test_city_id(self):
        self.assertEqual(str, type(Place.city_id))

    def test_name(self):
        self.assertEqual(str, type(Place.name))

    def test_number_rooms(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_latitude(self):
        self.assertEqual(float, type(Place.latitude))
    
    def test_amenity_ids(self):
        self.assertEqual(list, type(Place.amenity_ids))
