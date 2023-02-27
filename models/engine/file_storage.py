#!/usr/bin/python3
"""Shebang"""
import json
import os.path

class FileStorage:
    """Initialization of the class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Function that returns the dictionary (objects) from FileStorage class"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets a new object in __objects, with the class name as the key"""
        newKey = (f"{obj.__class__.__name__}.{str(obj.id)}")
        self.__class__.__objects[newKey] = obj
    
    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__class__.__file_path, 'w', encoding='utf-8') as f:
            objects_json = {}
            for key, value in self.__objects.items():
                objects_json[key] = value.to_dict()
            json.dump(objects_json, f)
    
    def reload(self):
        """Desearilzes the JSON file to __objects"""
        if os.path.isfile(self.__class__.__file_path):
            with open(self.__class__.__file_path, 'r', encoding='utf-8') as f:
                self.__class__.__objects = json.load(f)
