#!/usr/bin/python3
"""
Contains the subclass Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ creates an instance of an Amenity """

    name = ""

    def __init__(self):
        """ initializes Amenity """
        super(Amenity, self).__init__()
