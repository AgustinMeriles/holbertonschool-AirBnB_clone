#!/usr/bin/python3
"""Shebang"""
import uuid
import datetime
from models import storage


class BaseModel:
    """Initialization of class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor of the class"""

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the attribute with the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        newDict = self.__dict__.copy()
        newDict["__class__"] = type(self).__name__
        newDict["created_at"] = self.created_at.isoformat()
        newDict["updated_at"] = self.updated_at.isoformat()
        return newDict
