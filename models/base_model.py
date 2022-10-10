#!/usr/bin/python3
"""AirBnb more like HBNB"""

import uuid
import string
from datetime import datetime

class BaseModel:
    """Base model class"""
    def __init__(self, *args, **kwargs):
        """__init__"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"


    def __str__():
        """print [<class name>] (<self.id>) <self.__dict__>"""

    
    def save(self):
        """updates_at with the current datetime"""

    def to_dict(self):
        """returns dict countaining all keys/values of __dict__"""

