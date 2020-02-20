#!/usr/bin/python3
"""
Test module for the class Amenity
"""
from datetime import datetime
from models.amenity import Amenity
import unittest
import pep8


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of an Amenity """
        self.a1 = Amenity()

    def tearDown(self):
        """ tears down an instance of an Amenity """
        del self.a1

    def test_pep8(self):
        """ tests files to pep8 standard """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        a2 = Amenity()
        self.assertNotEqual(self.a1.id, a2.id)

    def test_attributes(self):
        """ tests attributes """
        self.a1.name = "Theater"
        self.assertTrue(hasattr(self.a1, "name"))
        self.assertIsInstance(self.a1.name, str)

    def test_str(self):
        """ test to check the string representation """
        self.a1.name = "Theater"
        string = "[{}] ({}) {}".format(self.a1.__class__.__name__,
                                       self.a1.id,
                                       self.a1.__dict__)
        self.assertEqual(str(self.a1), string)

    def test_format(self):
        """ test to check for time format """
        self.a1.save()
        a1_json = self.a1.to_dict()
        updated = self.a1.updated_at
        updated2 = datetime.strptime(a1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
