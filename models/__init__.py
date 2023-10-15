#!/usr/bin/python3
"""Initialization of the storage system for models."""
from models.engine.file_storage import FileStorage

# Create an instance of the FileStorage class
storage = FileStorage()
# Load data from the storage system
storage.reload()
