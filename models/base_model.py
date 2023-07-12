#!/usr/bin/python3
"""define the BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """defile the base model methods and fields"""

    def __init__(self):
        """the base model constructor"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        """string representation of base model"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """update the time of the model"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dictionnary representation"""

        diction = self.__dict__.copy()
        diction["__class__"] = self.__class__.__name__
        diction["created_at"] = self.created_at.isoformat()
        diction["updated_at"] = self.updated_at.isoformat()
        return diction
