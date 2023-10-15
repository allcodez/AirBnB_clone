#!/usr/bin/python3
"""Module that defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    Represents an abstracted storage engine for serializing and deserializing data.

    Attributes:
        __file_path (str): The path to the JSON file for saving objects.
        __objects (dict): A dictionary of objects with their unique identifiers as keys.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return a dictionary of all saved objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary with its class name and ID as the key."""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serialize the stored objects into a JSON file (__file_path)."""
        objects_dict = {obj_key: obj.to_dict() for obj_key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize the data from the JSON file (__file_path) and store it in the storage."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    self.new(eval(class_name)(**obj_dict))
        except FileNotFoundError:
            pass
