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
        self.assertNotEqual(a1.id, a2.id)

    def test_attributes(self):
        """ tests attributes """
        a1 = Amenity()
        a1.name = "Bedroom"
        self.assertIsInstance(a1, string)

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
        updated2 = datetime.strptime(a1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
