#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from models.state import State
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    
    if getenv("HBNB_TYPE_STORAGE") != "db":
        state_id = ""
        name = ""
    else:
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")
