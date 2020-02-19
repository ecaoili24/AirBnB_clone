#!/usr/bin/python3
"""
Test module for the class BaseModel
"""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of a BaseModel """
        self.model = BaseModel()

    def tearDown(self):
        """ tears down an instance of a BaseModel """
        del self.model

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertNotEqual(m1.id, m2.id)

    def test_attributes(self):
        """ tests attributes and save/update times """
        m1 = BaseModel()
        m1.name = "Pepe"
        m1.my_number = 24

        self.assertTrue(m1.name, "Pepe")
        self.assertTrue(m1.my_number, 24)

        created = m1.created_at
        updated = m1.updated_at
        m1.save()
        created2 = m1.created_at
        updated2 = m1.updated_at

        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)

    def test_str(self):
        """ test to check the string representation """
        m1 = BaseModel()
        m1.name = "Pepe"
        string = "[{}] ({}) {}".format(m1.__class__.__name__,
                                       m1.id,
                                       m1.__dict__)
        self.assertEqual(str(m1), string)

    def test_format(self):
        """ test to check for time format """
        m1 = BaseModel()
        m1.save()
        m1_json = m1.to_dict()
        updated = m1.updated_at
        updated2 = datetime.strptime(m1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
