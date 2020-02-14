#!/usr/bin/python3
"""
Contains the class BaseModel
"""

from datetime import datetime
import uuid


class BaseModel:
    """ base model used for other classes """

    def __init__(self):
        """ initializes the BaseModel """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ prints the string representation of the BaseModel """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the
        current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ """
        new_dict = self.__dict__.copy()
        new_dict[__class__] = self.__class__.__name__
        if "created_at" in new_dict:
            self.created_at = self.created_at.isoformat("%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in new_dict:
            self.updated_at = self.updated_at.isoformat("%Y-%m-%dT%H:%M:%S.%f")
        return new_dict
