#!/usr/bin/python3

"""
a class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import os

class FileStorage:
    """defining a class FileStorage"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_class_name = obj.__class__.__name__
        obj_id = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file1:
            obj_dict = {key: value.to_dict()
                    for key, value in FileStorage.__objects.items()}
            json.dump(obj_dict, file1)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file1:
            obj_dict = json.load(file1)
            FileStorage.__objects = obj_dict

