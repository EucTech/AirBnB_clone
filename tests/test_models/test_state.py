import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """To test for state"""
    def test_state_instance(self):
        """To test for state instance"""
        s = State()
        self.assertIsInstance(s, State)

    def test_state_attribute(self):
        """To test for attribute"""
        s = State()
        self.assertTrue(hasattr(s, 'name'))
