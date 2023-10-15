#!/usr/bin/python3
"""Defines unit tests for models/user.py.
Unit test classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User

class TestUserInstantiation(unittest.TestCase):
    """Unit tests for verifying the instantiation of the User class."""

    def test_no_args_instantiates(self):
        """Verify that User can be instantiated without arguments."""
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        """Ensure a newly created User instance is stored in the objects dictionary."""
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Check if the 'id' attribute of User is a string."""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Confirm that the 'created_at' attribute of User is a datetime object."""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """Verify that the 'updated_at' attribute of User is a datetime object."""
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        """Check if 'email' is a public class attribute of User."""
        us = User()
        self.assertEqual(str, type(User.email))
        self.assertIn("email", dir(us))
        self.assertNotIn("email", us.__dict__)

    def test_password_is_public_str(self):
        """Ensure that 'password' is a public class attribute of User."""
        us = User()
        self.assertEqual(str, type(User.password))
        self.assertIn("password", dir(us))
        self.assertNotIn("password", us.__dict__)

    def test_first_name_is_public_str(self):
        """Check that 'first_name' is a public class attribute of User."""
        us = User()
        self.assertEqual(str, type(User.first_name))
        self.assertIn("first_name", dir(us))
        self.assertNotIn("first_name", us.__dict__)

    def test_last_name_is_public_str(self):
        """Verify that 'last_name' is a public class attribute of User."""
        us = User()
        self.assertEqual(str, type(User.last_name))
        self.assertIn("last_name", dir(us))
        self.assertNotIn("last_name", us.__dict__)

    def test_two_users_unique_ids(self):
        """Ensure that two instances of User have different IDs."""
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_different_created_at(self):
        """Check that two instances of User have different 'created_at' timestamps."""
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        """Verify that two instances of User have different 'updated_at' timestamps."""
        us1 = User()
        sleep(0.05)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_str_representation(self):
        """Ensure the string representation of User is correct."""
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        us_str = us.__str__()
        self.assertIn("[User] (123456)", us_str)
        self.assertIn("'id': '123456'", us_str)
        self.assertIn("'created_at': " + dt_repr, us_str)
        self.assertIn("'updated_at': " + dt_repr, us_str)

    def test_args_unused(self):
        """Check that User ignores arguments during instantiation."""
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Verify instantiation of User with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Check that User raises a TypeError when instantiated with None values."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

class TestUserSave(unittest.TestCase):
    """Unit tests for testing the save method of the User class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Verify that saving a User instance updates the 'updated_at' attribute."""
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    def test_two_saves(self):
        """Check that saving a User instance multiple times updates the 'updated_at' attribute."""
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        second_updated_at = us.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        us.save()
        self.assertLess(second_updated_at, us.updated_at)

    def test_save_with_arg(self):
        """Verify that the save method raises a TypeError when given an argument."""
        us = User()
        with self.assertRaises(TypeError):
            us.save(None)

    def test_save_updates_file(self):
        """Ensure that saving a User instance updates the data file."""
        us = User()
        us.save()
        us_id = "User." + us.id
        with open("file.json", "r") as f:
            self.assertIn(us_id, f.read())

class TestUserToDict(unittest.TestCase):
    """Unit tests for testing the to_dict method of the User class."""

    def test_to_dict_type(self):
        """Check that the output of to_dict is a dictionary."""
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Verify that the keys in the to_dict output are correct."""
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Ensure that added attributes are present in the to_dict output."""
        us = User()
        us.middle_name = "Holberton"
        us.my_number = 98
        self.assertEqual("Holberton", us.middle_name)
        self.assertIn("my_number", us.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Check that the 'id', 'created_at', and 'updated_at' attributes in to_dict are strings."""
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        """Verify that the output of to_dict matches the expected dictionary."""
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        t_dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(us.to_dict(), t_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Ensure that the to_dict output is not the same as the __dict__ attribute."""
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        """Verify that the to_dict method raises a TypeError when given an argument."""
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(None)

if __name__ == "__main__":
    unittest.main()
