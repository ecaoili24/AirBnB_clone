#!/usr/bin/python3
"""
Contains the class FileStorage
"""

import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes dict __objects to the JSON file """
        serial = {}
        for key in self.__objects:
            serial[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serial, f)

    def reload(self):
        """ deserializes the JSON file to dict __objects """
        from models.base_model import BaseModel

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                j_object = json.load(f)
            for key, val in j_object.items():
                self.__objects[key] = BaseModel(**val)
        except:
            pass
