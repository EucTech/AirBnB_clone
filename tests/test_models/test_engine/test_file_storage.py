import unittest
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import uuid


class Test_FileStorage(unittest.TestCase):
    """To test for filestorage"""
    def setUp(self):
        """set up"""
        self.storage = FileStorage()

    def test_all_ins(self):
        """Tests for all instances"""
        obj = self.storage._FileStorage__objects
        self.assertIsInstance(obj, dict)

        for key, value in obj.items():
            self.assertIsInstance(value, object)

    def test_new(self):
        """Test if it creates a new instance"""
        b = BaseModel()
        key = "BaseModel." + b.id
        self.storage.new(b)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test if it saves instances"""
        b = BaseModel()
        key = "BaseModel." + b.id
        self.storage.new(b)
        self.storage.save()
        value = ""

        with open(self.storage._FileStorage__file_path, "r") as file:
            value = file.read()

        self.assertIn(key, value)
        self.assertIn(key, self.storage.all())

    def test_reload(self):
        """To check if the file reloads"""
        b = BaseModel()
        key = "BaseModel." + b.id
        self.storage.new(b)
        self.storage.save()

        new = FileStorage()
        new.reload()
        
        self.assertIn(key, new.all())
