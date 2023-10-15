#!/usr/bin/python3
"""Module that defines the City class."""
from models.base_model import BaseModel

class City(BaseModel):
    """
    Represents a city within the application.

    Attributes:
        state_id (str): The unique identifier of the state associated with the city.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
