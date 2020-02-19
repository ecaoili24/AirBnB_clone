#!/usr/bin/python3
"""
Test module for the class City
"""
from datetime import datetime
from models.city import City
import unittest


class TestCity(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of a City """
        self.city = City()

    def tearDown(self):
        """ tears down an instance of a City """
        del self.city

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_attributes(self):
        """ tests attributes and save/update times """
        c1 = City()
        c1.name = "San Francisco"
        c1.state_id = 24

        self.assertTrue(c1.name, "San Francisco")
        self.assertTrue(c1.state_id, 24)

        created = c1.created_at
        updated = c1.updated_at
        c1.save()
        created2 = c1.created_at
        updated2 = c1.updated_at

        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)

    def test_str(self):
        """ test to check the string representation """
        c1 = City()
        c1.name = "San Francisco"
        string = "[{}] ({}) {}".format(c1.__class__.__name__,
                                       c1.id,
                                       c1.__dict__)
        self.assertEqual(str(c1), string)

    def test_format(self):
        """ test to check for time format """
        c1 = City()
        c1.save()
        c1_json = c1.to_dict()
        updated = c1.updated_at
        updated2 = datetime.strptime(c1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
