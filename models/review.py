#!/usr/bin/python3
"""Module that defines the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Represents a review within the application.

    Attributes:
        place_id (str): The unique identifier of the place associated with the review.
        user_id (str): The unique identifier of the user who created the review.
        text (str): The text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
