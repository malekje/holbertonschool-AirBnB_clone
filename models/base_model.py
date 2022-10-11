#!/usr/bin/python3
"""AirBnb more like HBNB"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """Base model class"""
    def __init__(self, *args, **kwargs):
        """__init__"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            """key word arguements check & init attributes"""

        for key, val in kwargs.items():
            if key == "created_at" or key == "updated_at":
                val = datetime.strptime(val, date_format)
                if key != "__class__":
                    setattr(self, key, val)
        else:
            models.storage.new(self)




    def __str__(self):
        """print [<class name>] (<self.id>) <self.__dict__>"""
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dict countaining all keys/values of __dict__"""
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__['created_at'] = self.created_at.isoformat()

        return self.__dict__
