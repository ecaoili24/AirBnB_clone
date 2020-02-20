#!/usr/bin/python3
"""
Test module for the class Place
"""
from datetime import datetime
from models.place import Place
import uniitest


class TestPlace(unittest.TestCase):

    def setUp(self):
        """ sets up an instance of a Place """
        self.place = Place

    def tearDown(self):
        """ tears down an instance of a Place """
        del self.place

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_attributes(self):
        """ tests attributes to make sure they are strings/integers/floats """
        p1 = Place()
        self.assertIsInstance(p1.city_id, str)
        self.assertIsInstance(p1.user_id, str)
        self.assertIsInstance(p1.name, str)
        self.assertIsInstance(p1.description, str)
        self.assertIsInstance(p1.number_rooms, int)
        self.assertIsInstance(p1.number_bathrooms, int)
        self.assertIsInstance(p1.max_guest, int)
        self.assertIsInstance(p1.price_by_night, int)
        self.assertIsInstance(p1.latitude, float)
        self.assertIsInstance(p1.longitude, float)
        self.assertIsInstance(p1.amenity_ids, str)

    def test_str(self):
        """ test to check the string representation """
        p1 = Place()
        p1.name = "US"
        string = "[{}] ({}) {}".format(p1.__class__.__name__,
                                       p1.id,
                                       p1.__dict__)
        self.assertEqual(str(p1), string)

    def test_format(self):
        """ test to check for time format """
        p1 = Place()
        p1.save()
        p1_json = p1.to_dict()
        updated = p1.updated_at
        updated2 = datetime.strptime(p1_json["updated_at"],
                                     "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)
