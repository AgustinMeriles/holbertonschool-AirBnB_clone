#!/usr/bin/python3
"""unittests for base_model.py"""
import unittest
from models.base_model import BaseModel


class test_base_basics(unittest.TestCase):
    def test_string(self):
        my_model = BaseModel()
        my_model.name = "Something"
        self.assertEqual(my_model.name, "Something")

    def test_timestamp_create(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.created_at)

    def test_timestamp_update(self):
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)


class test_base_dict(unittest.TestCase):
    def test_dict(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertEqual(str(type(my_model_dict)), "<class 'dict'>")

    def test_recreation(self):
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.name, my_new_model.name)

    def test_recreation_datetype(self):
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        print(type(my_model.created_at))
        print(type(my_new_model.created_at))
        self.assertEqual(type(my_model.created_at),type(my_new_model.created_at))


if __name__ == "__main__":
    unittest.main()
