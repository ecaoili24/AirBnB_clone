#!/usr/bin/python3
"""
Test module for the class Review
"""
from datetime import datetime
from models.review import Review
import unittest


class TestReview(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of a Review """
        self.review = Review()

    def tearDown(self):
        """ tears down an instance of a Review """
        del self.review

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_attributes(self):
        """ tests attributes """
        r1 = Review()
        self.assertIsInstance(r1.place_id, str)
        self.assertIsInstance(r1.user_id, str)
        self.assertIsInstance(r1.text, str)

    def test_str(self):
        """ test to check the string representation """
        r1 = Review()
        r1.name = "5 Stars"
        string = "[{}] ({}) {}".format(r1.__class__.__name__,
                                       r1.id,
                                       r1.__dict__)
        self.assertEqual(str(r1), string)

    def test_format(self):
        """ test to check for time format """
        r1 = Review()
        r1.save()
        r1_json = r1.to_dict()
        updated = r1.updated_at
        updated2 = datetime.strptime(r1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
