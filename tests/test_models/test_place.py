import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """To test for place"""
    def test_place_instance(self):
        """To test for instance"""
        p = Place()
        self.assertIsInstance(p, Place)

    def test_place_attribute(self):
        """To test for attribute"""
        p = Place()
        self.assertTrue(p, 'city_id')
        self.assertTrue(p, 'user_id')
        self.assertTrue(p, 'name')
        self.assertTrue(p, 'description')
        self.assertTrue(p, 'number_rooms')
        self.assertTrue(p, 'number_bathrooms')
        self.assertTrue(p, 'max_guest')
        self.assertTrue(p, 'price_by_night')
        self.assertTrue(p, 'latitude')
        self.assertTrue(p, 'longitude')
        self.assertTrue(p, 'amenity_ids')
