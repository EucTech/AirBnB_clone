import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """To test for review"""
    def test_review_instance(self):
        """To test for instance"""
        r = Review()
        self.assertIsInstance(r, Review)

    def test_review_attribute(self):
        """To test for attribute"""
        r = Review()
        self.assertTrue(hasattr(r, 'place_id'))
        self.assertTrue(hasattr(r, 'user_id'))
        self.assertTrue(hasattr(r, 'text'))
