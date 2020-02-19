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
        self.user = User()

    def tearDown(self):
        """ tears down an instance of a User """
        del self.user

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_attributes(self):
        """ tests attributes and save/update times """
        u1 = User()
        u1.email = "pepe.python@hbnb.com"
        u1.password = "pep8"
        u1.first_name = "Pepe"
        u1.last_name = "Python"

        self.assertTrue(u1.email, "pepe.python@hbnb.com")
        self.assertTrue(u1.password, "pep8")
        self.assertTrue(u1.first_name, "Pepe")
        self.assertTrue(u1.last_name, "Python")

        created = u1.created_at
        updated = u1.updated_at
        u1.save()
        created2 = u1.created_at
        updated2 = u1.updated_at

        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)

    def test_str(self):
        """ test to check the string representation """
        u1 = User()
        u1.first_name = "Pepe"
        string = "[{}] ({}) {}".format(u1.__class__.__name__,
                                       u1.id,
                                       u1.__dict__)
        self.assertEqual(str(u1), string)

    def test_format(self):
        """ test to check for time format """
        u1 = User()
        u1.save()
        u1_json = u1.to_dict()
        updated = u1.updated_at
        updated2 = datetime.strptime(u1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
