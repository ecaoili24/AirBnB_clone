#!/usr/bin/python3
"""
Test module for the class Amenity
"""
from datetime import datetime
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of an Amenity """
        self.amenity = Amenity()

    def tearDown(self):
        """ tears down an instance of an Amenity """
        del self.amenity

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(c1.id, c2.id)

    def test_attributes(self):
        """ tests attributes and save/update times """
        a1 = Amenity()
        a1.name = "Bedroom"

        self.assertTrue(c1.name, "Bedroom")

        created = a1.created_at
        updated = a1.updated_at
        a1.save()
        created2 = a1.created_at
        updated2 = a1.updated_at

        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)

    def test_str(self):
        """ test to check the string representation """
        a1 = Amenity()
        a1.name = "Bedroom"
        string = "[{}] ({}) {}".format(a1.__class__.__name__,
                                       a1.id,
                                       a1.__dict__)
        self.assertEqual(str(a1), string)

    def test_format(self):
        """ test to check for time format """
        a1 = Amenity()
        a1.save()
        a1_json = a1.to_dict()
        updated = a1.updated_at
        updated2 = datetime.strptime(c1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
