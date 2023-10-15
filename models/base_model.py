#!/usr/bin/python3
"""Module that defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Represents the BaseModel class, the core of the HBnB project.

    Attributes:
        id (str): A unique identifier generated for each instance.
        created_at (datetime): The creation date and time of the instance.
        updated_at (datetime): The last update date and time of the instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): A dictionary of key-value pairs representing attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        Update the 'updated_at' attribute with the current date and time
        and save the instance.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance,
        including key-value pairs for 'created_at' and 'updated_at',
        as well as the '__class__' attribute representing the class name.
        """
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        The representation includes the class name, the instance ID, and
        a dictionary of attributes.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
