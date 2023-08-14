import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test for amenity"""
    def test_instance(self):
        """To check for instance"""
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_attribute(self):
        """To check the attribute of the class"""
        a = Amenity()
        self.assertTrue(hasattr(a, 'name'))
