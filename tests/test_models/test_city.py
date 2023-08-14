#!/usr/bin/python3
"""Unittest module for the City Class"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """To test for city"""
    def test_city_instance(self):
        """To check for instance"""
        c = City()
        self.assertIsInstance(c, City)

    def test_city_attribute(self):
        """To check for attributes"""
        c = City()
        self.assertTrue(hasattr(c, 'state_id'))
        self.assertTrue(hasattr(c, 'name'))
