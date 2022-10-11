#!/usr/bin/python3
"""AirBnb more like HBNB"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """Base model class"""
    def __init__(self, *args, **kwargs):
        """__init__"""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            """key word arguements check & init attributes"""
        for key, Value in kwargs.items():
            if key == "created_at" or key == "updated_at":
                Value = datetime.strptime(Value, date_format)
                if key != "__class__":
                    setattr(self, key, Value)
        else:
            models.storage.new(self)

            def __str__():
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
        self.__dict__['update_at'] = self.updated_at.isoformat()
        self.__dict__['created_at'] = self.created_at.isoformat()

        return self.__dict__
