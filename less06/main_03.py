# Работа с полями моделей данных
# Для валидации данных можно использовать следующие параметры при создании моделей:
# ● default: значение по умолчанию для поля
# ● alias: альтернативное имя для поля (используется при сериализации и десериализации)
# ● title: заголовок поля для генерации документации API
# ● description: описание поля для генерации документации API
# ● gt: ограничение на значение поля (больше указанного значения)
# ● ge: ограничение на значение поля (больше или равно указанному значению)
# ● lt: ограничение на значение поля (меньше указанного значения)
# ● le: ограничение на значение поля (меньше или равно указанному значению)
# ● multiple_of: ограничение на значение поля (должно быть кратно указанному значению)
# ● max_length: ограничение на максимальную длину значения поля
# ● min_length: ограничение на минимальную длину значения поля
# ● regex: регулярное выражение, которому должно соответствовать значение поля


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(..., title="Name", max_length=50)  # ... означает что поле обязательно!!
    price: float = Field(..., title="Price", gt=0, le=100000)
    description: str = Field(default=None, title="Description", max_length=1000)
    tax: float = Field(0, title="Tax", ge=0, le=10)


class User(BaseModel):
    username: str = Field(title="Username", max_length=50)
    full_name: str = Field(None, title="Full Name", max_length=100)  # None поле необязательно
