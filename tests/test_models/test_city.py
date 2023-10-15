#!/usr/bin/python3
"""Defines unit tests for models/city.py.

Unittest classes:
    TestCityInstantiation
    TestCitySave
    TestCityToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    """Unit tests for testing the instantiation of the City class."""

    def test_no_args_instantiates(self):
        """Test if City can be instantiated with no arguments."""
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance is stored in the objects dictionary."""
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if the 'id' attribute is a public string."""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        """Test if the 'created_at' attribute is a public datetime."""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if the 'updated_at' attribute is a public datetime."""
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_class_attribute(self):
        """Test if 'state_id' is a public class attribute."""
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_is_public_class_attribute(self):
        """Test if 'name' is a public class attribute."""
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_two_cities_unique_ids(self):
        """Test if two instances have unique IDs."""
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_two_cities_different_created_at(self):
        """Test if two instances have different 'created_at' times."""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_two_cities_different_updated_at(self):
        """Test if two instances have different 'updated_at' times."""
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    def test_str_representation(self):
        """Test the string representation of an instance."""
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cy_str = cy.__str__()
        self.assertIn("[City] (123456)", cy_str)
        self.assertIn("'id': '123456'", cy_str)
        self.assertIn("'created_at': " + dt_repr, cy_str)
        self.assertIn("'updated_at': " + dt_repr, cy_str)

    def test_args_unused(self):
        """Test instantiation with unused arguments."""
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """Test instantiation with keyword arguments."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation with None as keyword arguments."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCitySave(unittest.TestCase):
    """Unit tests for testing the save method of the City class."""

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
        """Test the 'save' method with a single call."""
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    def test_two_saves(self):
        """Test the 'save' method with multiple calls."""
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    def test_save_with_arg(self):
        """Test the 'save' method with an argument."""
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_updates_file(self):
        """Test if the 'save' method updates the 'file.json' file."""
        cy = City()
        cy.save()
        cy_id = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cy_id, f.read())


class TestCityToDict(unittest.TestCase):
    """Unit tests for testing the to_dict method of the City class."""

    def test_to_dict_type(self):
        """Test the type of the 'to_dict' method's output."""
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if 'to_dict' contains the correct keys."""
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if 'to_dict' contains added attributes."""
        cy = City()
        cy.middle_name = "Holberton"
        cy.my_number = 98
        self.assertEqual("Holberton", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes in 'to_dict' are strings."""
        cy = City()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of the 'to_dict' method."""
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        t_dict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), t_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test the difference between 'to_dict' and '__dict__'."""
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)

    def test_to_dict_with_arg(self):
        """Test the 'to_dict' method with an argument."""
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)


if __name__ == "__main__":
    unittest.main()
