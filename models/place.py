#!/usr/bin/python3
"""Place Class"""



from models.base_model import BaseModel


int = 0
float = 0.0


class Place(BaseModel):
    """Place Class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = int
    number_bathrooms = int
    max_guest = int
    price_by_night = int
    latitude = float
    longitude = float
    amenity_ids = []
