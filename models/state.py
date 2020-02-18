#!/usr/bin/python3
"""
Contains the subclass State
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ creates an instance of a State """

    name = ""

    def __init__(self):
        """ initializes State """
        super(State, self).__init__()
