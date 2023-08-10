import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.b = BaseModel()

    def test__init__(self):
        """To check generated uuid"""
        generated_id = str(uuid.UUID(self.b.id, version=4))
        self.assertEqual(self.b.id, generated_id)

    def test__init__string(self):
        """To check if the id is a string"""
        self.assertIsInstance(self.b.id, str)

    def test_created_at(self):
        """To check the the time an instance is created"""
        value = datetime.now()
        self.assertTrue(self.b.created_at, value)

    def test_updated_at(self):
        """To check the time the instance is updated"""
        value = datetime.now()
        self.assertTrue(self.b.updated_at, value)

    def test__str__(self):
        """To test the string reprensentation"""
        value = f"[{self.b.__class__.__name__}] ({self.b.id}) {self.b.__dict__}"
        self.assertEqual(self.b.__str__(), value)

    def test_to_dict(self):
        """To test the dictionary respresetation of instance"""
        value = {
            'id': self.b.id,
            'created_at': self.b.created_at.isoformat(),
            'updated_at': self.b.updated_at.isoformat(),
            '__class__': self.b.__class__.__name__
        }
        self.assertEqual(self.b.to_dict(), value)
