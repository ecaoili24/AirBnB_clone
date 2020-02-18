#!/usr/bin/python3
"""
Contains the subclass User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ creates an instance of a User """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """ initializes User """
        super(User, self).__init__()
