from pydantic import BaseModel
from typing import List


class Attraction(BaseModel):
    id: str
    name: str
    latitude: float
    longitude: float
    price: float
    rating: float


class Point(BaseModel):
    latitude: float
    longitude: float


class PathInput(BaseModel):
    start_point: Point
    max_distance: float
    min_rating: float
    max_price: float
    nr_attractions: int
    attractions: List[Attraction]


class PromptInput(BaseModel):
    prompt: str
