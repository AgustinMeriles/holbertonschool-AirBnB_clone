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

    def test_user_first_name(self):
        """ Testing User attributes"""
        var = User()
        self.assertEqual(var.first_name, "")

    def test_user_last_name(self):
        """ Testing User attributes"""
        var = User()
        self.assertEqual(var.last_name, "")

    def test_user_email(self):
        """ Testing User attributes"""
        var = User()
        self.assertEqual(var.email, "")

    def test_user_password(self):
        """ Testing User attributes"""
        var = User()
        self.assertEqual(var.password, "")

    def test_city_state_id(self):
        """ Testing City attributes """
        var = City()
        self.assertEqual(var.state_id, "")

    def test_city_name(self):
        """ Testing City attributes """
        var = City()
        self.assertEqual(var.name, "")

    def test_amenity(self):
        """ Testing amenity attributes """
        var = Amenity()
        self.assertEqual(var.name,"")

    def test_place_city_id(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.city_id, "")

    def test_place_user_id(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.user_id, "")

    def test_place_name(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.name, "")

    def test_place_description(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.description, "")
        
    def test_place_number_rooms(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.number_rooms, 0)

    def test_place_number_bathrooms(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.number_bathrooms, 0)

    def test_place_max_guests(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.max_guest, 0)

    def test_place_price_night(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.price_by_night, 0)

    def test_place_latitude(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.latitude, 0.0)

    def test_place_longitude(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.longitude, 0.0)

    def test_place_amenity_id(self):
        """ Testing Place attributes """
        var = Place()
        self.assertEqual(var.amenity_ids, [])

    def test_review_place_id(self):
        """ Testing Review attributes """
        var = Review()
        self.assertEqual(var.place_id, "")

    def test_review_user_id(self):
        """ Testing Review attributes """
        var = Review()
        self.assertEqual(var.user_id, "")

    def test_review_text(self):
        """ Testing Review attributes """
        var = Review()
        self.assertEqual(var.text, "")

    def test_state(self):
        """ Testing State attributes """
        var = State()
        self.assertEqual(var.name, "")
