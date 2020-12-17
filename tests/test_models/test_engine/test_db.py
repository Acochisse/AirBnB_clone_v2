#!/usr/bin/python3

import unittest
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "only testing db storage")
class test_DBStorage(unittest.TestCase):

    def testUser(self):
        user = User(name="Case")
        if user.id in models.storage.all():
            self.assertTrue(user.name, "Case")


    def testState(self):
        state = State(name="Chiba")
        if state.id in models.storage.all():
            self.assertTrue(state.name, "Chiba")

    def testCity(self):
        city = City(name="Night City")
        if city.id in models.storage.all():
            self.assertTrue(city.name, "Night City")

    def testPlace(self):
        place = Place(name="Cheap Hotel", number_rooms=5)
        if place.id in models.storage.all():
            self.assertTrue(place.number_rooms, 5)
            self.assertTrue(place.name, "Cheap Hotel")


    def testAmenity(self):
        amenity = Amenity(name="2 Bath")
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, "2 Bath")

    def testReview(self):
        review = Review(text="Bombed out foxhole on mars")
        if review.id in models.storage.all():
            self.assertTrue(review.text, "Bombed out foxhole on mars")

    def teardown(self):
        self.session.close()
        self.session.rollback()
