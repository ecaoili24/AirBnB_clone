#!/usr/bin/python3
"""
Test module for the class City
"""
from datetime import datetime
from models.state import State
import unittest


class TestState(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of a State """
        self.state = State()

    def tearDown(self):
        """ tears down an instance of a State """
        del self.state

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        s1 = State()
        s2 = State()
        self.assertNotEqual(c1.id, c2.id)

    def test_attributes(self):
        """ tests attributes and save/update times """
        s1 = State()
        s1.name = "California"
        s1.state_id = 24

        self.assertTrue(s1.name, "California")
        self.assertTrue(s1.state_id, 24)

        created = s1.created_at
        updated = s1.updated_at
        s1.save()
        created2 = s1.created_at
        updated2 = s1.updated_at

        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)

    def test_str(self):
        """ test to check the string representation """
        s1 = State()
        s1.name = "California"
        string = "[{}] ({}) {}".format(s1.__class__.__name__,
                                       s1.id,
                                       s1.__dict__)
        self.assertEqual(str(s1), string)

    def test_format(self):
        """ test to check for time format """
        s1 = State()
        s1.save()
        s1_json = s1.to_dict()
        updated = s1.updated_at
        updated2 = datetime.strptime(s1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
