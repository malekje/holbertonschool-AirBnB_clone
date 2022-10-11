#!/usr/bin/python3

"""AirBnb more like HBNB"""

from models.base_model import BaseModel
import json

class FileStorage:
    """ class that serializes instances to a JSON file """

    
    __file_path = "file.json"
    __objects = {}

    

    def all(self):
        """ returns the dictionary objects """
        return self.__objects

    def new(self, obj):
        """ set inobjects the obj with key """

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file  """
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(new_dict, f)
   
    def reload(self):
        """ deserializes the JSON file """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj = json.load(f)
            for k, v in obj.items():
                class_name = k.split('.')[0]
                self.__objects[k] = eval(class_name)(**v)
        except BaseException:
            pass
