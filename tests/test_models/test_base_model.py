#!/usr/bin/python3
"""Unit Test fo BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid

class TestBaseModel(unittest.TestCase):
    """A test for BaseModel class"""

    def test_default_attr(self):
