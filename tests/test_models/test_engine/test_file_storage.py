#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import os


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class"""

    def setUp(self):
        """setting up"""
        self.storage = FileStorage()

    def tearDown(self):
        """tearing down"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init(self):
        """tstinf class attributes"""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_all(self):
        """testing the all method"""
        obj_dict = self.storage.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict, FileStorage._FileStorage__objects)

    def test_new(self):
        """testing the new method"""

    def test_save(self):
        """testing the save method"""
        self.storage.save()
        with open("file.json", "r", encoding="utf-8") as file1:
            self.assertIn(id, file1.readline())
        with self.assertRaises(TypeError):
            self.storage.save(1)

    def test_reload(self):
        """testing reload method"""
        self.storage.reload()
        self.assertIn(id, self.storage.all())
        with self.assertRaises(TypeError):
            self.storage.reload(1)
