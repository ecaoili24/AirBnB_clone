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
        new_dict['__class__'] = str(self.__class__.__name__)
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
