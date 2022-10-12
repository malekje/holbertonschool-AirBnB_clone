#!/usr/bin/python3
""" user class """


import email
from models.base_model import BaseModel


class user(BaseModel):
    """ user's class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
