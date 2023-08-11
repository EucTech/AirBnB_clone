#!/usr/bin/python3

"""
a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """defining a class FileStorage"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """function that adds a new instance to the __objects
            dictionary"""
        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as file1:
            obj_dict = {key: value.to_dict()
                    for key, value in self.__objects.items()}
            json.dump(obj_dict, file1)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r", encoding="utf-8") as file1:
                    obj_dict = json.load(file1)

                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    cls = eval(class_name)
                    class_instance = cls(**value)
                    self.__objects[key] = class_instance
            except Exception as e:
                    pass
