#!/usr/bin/python3
"""
    This is the base model that defines
    all the attributes and methods of other classes
"""
import uuid
from datetime import datetime
# from models import storage
import models


class BaseModel():
    """This is the base class"""
    def __init__(self, *args, **kwargs):
        """Instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        value =\
                               datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    if key == "updated_at":
                        value =\
                               datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """This is a string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This gets the time a file is saved"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
            This is the dictiontary represation of the
            instance attributes and the class name
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
