#!/usr/bin/python3
<<<<<<< HEAD
"""
    contains state class to represent a state
"""

from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
=======
"""State Class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
>>>>>>> 349642e593f860b031140b012c6861d3396e21e9
from sqlalchemy.orm import relationship
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")

<<<<<<< HEAD

class State(BaseModel, Base):
    """ State class: class to represent states of cities"""
    if (storage_engine == 'db'):
        __tablename__ = "states"
=======
class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
>>>>>>> 349642e593f860b031140b012c6861d3396e21e9
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

<<<<<<< HEAD
        @property
        def cities(self):
            """cities list
            """
            result = []
            for j, i in models.storage.all(models.city.City).items():
                if (i.state_id == self.id):
                    result.append(i)
            return result

=======
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
>>>>>>> 349642e593f860b031140b012c6861d3396e21e9
