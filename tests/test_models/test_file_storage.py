#!/usr/bin/python3
"""
Test module for class FileStorage
"""
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import unittest
import pep8
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of a FileStorage """
        self.f1 = FileStorage()

    def tearDown(self):
        """ tears down an instance of a FileStorage """
        del self.f1

    def test_pep8(self):
        """ tests files to pep8 standard """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_all(self):
        """ tests all method """
        storage.reload()
        self.assertIsInstance(self.f1.all(), dict)

    def test_new(self):
        """ tests new method """
        self.f1.new(BaseModel())
        self.assertTrue(self.f1.all())

    def test_save(self):
        """ tests save method """
        storage.reload()
        self.f1.new(BaseModel())
        self.f1.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_reload(self):
        """ tests reload method """
        storage.reload()
        model = BaseModel()
        key = "BaseModel" + "." + model.id
        self.f1.new(model)
        self.f1.save()
        self.f1.reload()
        self.assertTrue(self.f1.all()[key])
