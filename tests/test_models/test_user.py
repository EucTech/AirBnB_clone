import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """To test for user"""

    def test_user_instance(self):
        """To test for instance"""
        u = User()
        self.assertIsInstance(u, User)

    def test_user_attribute(self):
        """To test for attribute"""
        u = User()
        self.assertTrue(hasattr(u, 'email'))
        self.assertTrue(hasattr(u, 'password'))
        self.assertTrue(hasattr(u, 'first_name'))
        self.assertTrue(hasattr(u, 'last_name'))
