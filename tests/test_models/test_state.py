#!/usr/bin/python3
"""
Test module for the class State
"""
from datetime import datetime
from models.state import State
import unittest
import pep8


class TestState(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of a State """
        self.s1 = State()

    def tearDown(self):
        """ tears down an instance of a State """
        del self.s1

    def test_pep8(self):
        """ tests files to pep8 standard """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        s2 = State()
        self.assertNotEqual(self.s1.id, s2.id)

    def test_attributes(self):
        """ tests attributes and save/update times """
        self.s1.name = "California"
        self.assertTrue(hasattr(self.s1, "name"))
        self.assertIsInstance(self.s1.name, str)

        created = self.s1.created_at
        updated = self.s1.updated_at
        self.s1.save()
        created2 = self.s1.created_at
        updated2 = self.s1.updated_at

        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)

    def test_str(self):
        """ test to check the string representation """
        self.s1.name = "California"
        string = "[{}] ({}) {}".format(self.s1.__class__.__name__,
                                       self.s1.id,
                                       self.s1.__dict__)
        self.assertEqual(str(self.s1), string)

    def test_format(self):
        """ test to check for time format """
        self.s1.save()
        s1_json = self.s1.to_dict()
        updated = self.s1.updated_at
        updated2 = datetime.strptime(s1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
