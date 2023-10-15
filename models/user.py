#!/usr/bin/python3
"""Module that defines the User class."""
from models.base_model import BaseModel

class User(BaseModel):
    """
    Represents a user within the application.

    Attributes:
        email (str): The email address of the user.
        password (str): The user's password.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
