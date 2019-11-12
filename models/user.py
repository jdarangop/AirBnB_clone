#!/usr/bin/python3
""" User Module that Inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class Used to represent an User
        Attributes
        ----------
        email : str
            email of the user
        password: str
            password of the user
        first_name: str
            first legal name of the user
        last_name: str
            last legal name of the user
    """

    def __init__(self, *args, **kwargs):
        """ Parameters
            ----------
        email : str
            email of the user
        password: str
            password of the user
        first_name: str
            first legal name of the user
        last_name: str
            last legal name of the user
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
