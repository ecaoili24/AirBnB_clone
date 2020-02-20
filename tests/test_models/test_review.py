#!/usr/bin/python3
"""
Test module for the class Review
"""
from datetime import datetime
import pep8
from models.review import Review
import unittest


class TestReview(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of a Review """
        self.r1 = Review()

    def tearDown(self):
        """ tears down an instance of a Review """
        del self.r1

    def test_pep8(self):
        """ tests files to pep8 standard """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        r2 = Review()
        self.assertNotEqual(self.r1.id, r2.id)

    def test_attributes(self):
        """ tests attributes """
        self.assertTrue(hasattr(self.r1, "place_id"))
        self.assertTrue(hasattr(self.r1, "user_id"))
        self.assertTrue(hasattr(self.r1, "text"))
        self.assertIsInstance(self.r1.place_id, str)
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.text, str)

    def test_str(self):
        """ test to check the string representation """
        self.r1.name = "5 Stars"
        string = "[{}] ({}) {}".format(self.r1.__class__.__name__,
                                       self.r1.id,
                                       self.r1.__dict__)
        self.assertEqual(str(self.r1), string)

    def test_format(self):
        """ test to check for time format """
        self.r1.save()
        r1_json = self.r1.to_dict()
        updated = self.r1.updated_at
        updated2 = datetime.strptime(r1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
