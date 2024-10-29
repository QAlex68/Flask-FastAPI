# Определение моделей данных
# Pydantic — это библиотека для валидации данных и сериализации объектов Python.
# Она используется в FastAPI для валидации данных, получаемых из запросов, и
# генерации документации API на основе моделей данных

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


class User(BaseModel):
    username: str
    full_name: str = None


class Order(BaseModel):
    items: List[Item]
    user: User
