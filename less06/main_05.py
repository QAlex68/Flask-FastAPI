# Работа с базой данных - Создание подключения к базе данных
# pip install sqlalchemy
# pip install databases[aiosqlite]

import databases
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = "sqlite:///mydatabase.db"
# Подключение к PostgreSQL
# Если мы хотим зменить SQLite на PostgreSQL, достоточно заменить данные в константе подключения к БД:
# DATABASE_URL = "postgresql://user:password@localhost/dbname"
# Указав тип базы данных, имя пользователя, пароль, хост и название базы данных мы установим с ней соединение.

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
...
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
