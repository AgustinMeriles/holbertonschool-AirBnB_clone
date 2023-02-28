#!/usr/bin/python3
""" Tests for specific modules
Modules tested:
- User
- City
- Amenity
- Place
- Review
- State """
import unittest
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State




class Tests(unittest.TestCase):
    """ Test functions for modules"""

    def test_user(self):
        """ Testing User attributes"""
        var = User()
        self.assertEqual(var.first_name, "")
        self.assertEqual(var.last_name, "")
        self.assertEqual(var.email, "")
        self.assertEqual(var.password, "")

    def test_city(self):
        """ Testing City attributes """
        var = City()
        self.assertEqual(var.state_id, "")
        self.assertEqual(var.name, "")

    def test_amenity(self):
        """ Testing amenity attributes """
        var = Amenity()
        self.assertEqual(var.name,"")

    def test_place(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.city_id, "")
        self.assertEqual(var.user_id, "")
        self.assertEqual(var.name, "")
        self.assertEqual(var.description, "")
        self.assertEqual(var.number_rooms, 0)
        self.assertEqual(var.number_bathrooms, 0)
        self.assertEqual(var.max_guest, 0)
        self.assertEqual(var.price_by_night, 0)
        self.assertEqual(var.latitude, 0.0)
        self.assertEqual(var.longitude, 0.0)
        self.assertEqual(var.amenity_ids, [])

    def test_review(self):
        """ Testing Review attributes """
        var = Review()
        self.assertEqual(var.place_id, "")
        self.assertEqual(var.user_id, "")
        self.assertEqual(var.text, "")


    def test_state(self):
        """ Testing State attributes """
        var = State()
        self.assertEqual(var.name, "")
