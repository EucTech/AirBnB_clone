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
        """
            1. It open the file specified by self.__file_path
            2. It creates a dictionary object called obj_dict
            that holds the serialized form of the instance stored
            in __objects
            3. to.dict method is called for each key-value instance to
            convert the instance into a dictionary represention, and
            assigns it to obj_dict.
            4. It iterates over the items key & value in self.__objects
            using dictionary comprehension
            5 Serializes __objects to the JSON file
        """
        with open(self.__file_path, "w", encoding="utf-8") as file1:
            obj_dict = {key: value.to_dict()
                    for key, value in self.__objects.items()}
            json.dump(obj_dict, file1)

    def reload(self):
        """
            1. Check if the file created from self.__object
            exists, then open it and read through it.
            2. Deserializes the JSON file to __objects.
            3 Use for loop to iterate through key-value of obj_dict
            dictionary to recreate the instances from that obj_dict
            4 Extract the value of __class__
            5 using eval to convert a string representation of a class
            into the actual class type
            6 **value: The double asterisk ** is used for dictionary
            unpacking. It takes the key-value pairs from the dictionary
            value and passes them as keyword arguments to the class
            constructor. In other words, it "unpacks" the dictionary
            into individual arguments for the constructor.
            7 The line self.new(class_instance) is calling the new method
            of the FileStorage class to add a newly created instance
            to the __objects dictionary

        """
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r", encoding="utf-8") as file1:
                    obj_dict = json.load(file1)

                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    cls = eval(class_name)
                    class_instance = cls(**value)
                    self.new(class_instance)
            except Exception as e:
                pass
