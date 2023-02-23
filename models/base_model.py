#!/usr/bin/python3
"""Shebang"""
import uuid
import datetime


class BaseModel:
    """Initialization of class BaseModel"""

    def __init__(self):
        """Constructor of the class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.update_at = self.created_at

    def __str__(self):
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the attribute with the current datetime"""
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        newDict = self.__dict__.copy()
        newDict["__class__"] = type(self).__name__
        newDict["created_at"] = self.created_at.isoformat()
        newDict["updated_at"] = self.update_at.isoformat()
        return newDict
