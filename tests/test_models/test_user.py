#!/usr/bin/python3
"""
Test module for the class User
"""
from datetime import datetime
from models.user import User
import unittest


class TestUser(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of a User """
        self.u1 = User()

    def tearDown(self):
        """ tears down an instance of a User """
        del self.u1

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        u2 = User()
        self.assertNotEqual(self.u1.id, u2.id)

    def test_attributes(self):
        """ tests attributes to make sure they are string """
        self.assertIsInstance(self.u1.email, str)
        self.assertIsInstance(self.u1.password, str)
        self.assertIsInstance(self.u1.first_name, str)
        self.assertIsInstance(self.u1.last_name, str)

    def test_str(self):
        """ test to check the string representation """
        self.u1.first_name = "Pepe"
        string = "[{}] ({}) {}".format(self.u1.__class__.__name__,
                                       self.u1.id,
                                       self.u1.__dict__)
        self.assertEqual(str(self.u1), string)

    def test_format(self):
        """ test to check for time format """
        self.u1.save()
        u1_json = self.u1.to_dict()
        updated = self.u1.updated_at
        updated2 = datetime.strptime(u1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
