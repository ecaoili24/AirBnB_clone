#!/usr/bin/python3
"""
Test module for the class Place
"""
from datetime import datetime
from models.place import Place
import unittest
import pep8


class TestPlace(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of a Place """
        self.p1 = Place()

    def tearDown(self):
        """ tears down an instance of a Place """
        del self.p1

    def test_pep8(self):
        """ tests files to pep8 standard """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        p2 = Place()
        self.assertNotEqual(self.p1.id, p2.id)

    def test_attributes(self):
        """ tests attributes to make sure they are strings/integers/floats """
        self.assertIsInstance(self.p1.city_id, str)
        self.assertIsInstance(self.p1.user_id, str)
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.longitude, float)
        self.assertIsInstance(self.p1.amenity_ids, str)

    def test_has_attr(self):
        """ test to make sure class has attributes """
        self.assertTrue(hasattr(self.p1, "city_id"))
        self.assertTrue(hasattr(self.p1, "user_id"))
        self.assertTrue(hasattr(self.p1, "name"))
        self.assertTrue(hasattr(self.p1, "description"))
        self.assertTrue(hasattr(self.p1, "number_rooms"))
        self.assertTrue(hasattr(self.p1, "number_bathrooms"))
        self.assertTrue(hasattr(self.p1, "max_guest"))
        self.assertTrue(hasattr(self.p1, "price_by_night"))
        self.assertTrue(hasattr(self.p1, "latitude"))
        self.assertTrue(hasattr(self.p1, "longitude"))
        self.assertTrue(hasattr(self.p1, "amenity_ids"))

    def test_str(self):
        """ test to check the string representation """
        self.p1.name = "US"
        string = "[{}] ({}) {}".format(self.p1.__class__.__name__,
                                       self.p1.id,
                                       self.p1.__dict__)
        self.assertEqual(str(self.p1), string)

    def test_format(self):
        """ test to check for time format """
        self.p1.save()
        p1_json = self.p1.to_dict()
        updated = self.p1.updated_at
        updated2 = datetime.strptime(p1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
