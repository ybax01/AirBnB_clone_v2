<<<<<<< HEAD
#!/usr/bin/python3
"""
    contains City class to represent a city
    contains City class to represent a city
"""

from models.base_model import BaseModel, Base
from models.state import State
=======
#!/usr/bin/python
""" City Class """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
>>>>>>> 349642e593f860b031140b012c6861d3396e21e9
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
<<<<<<< HEAD
    """ City class :City class to represent a city
    City class :City class to represent a city"""

    if (storage_engine == "db"):
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey(State.id))
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        name = ""
        state_id = ""

=======
    """Representation of city """
    if models.storage_t == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
>>>>>>> 349642e593f860b031140b012c6861d3396e21e9
