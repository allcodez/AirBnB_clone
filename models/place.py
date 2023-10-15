#!/usr/bin/python3
"""Module that defines the Place class."""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    Represents a place within the application.

    Attributes:
        city_id (str): The unique identifier of the city associated with the place.
        user_id (str): The unique identifier of the user who owns the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The total number of rooms in the place.
        number_bathrooms (int): The total number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can accommodate.
        price_by_night (int): The nightly price of the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of unique identifiers for associated amenities.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
