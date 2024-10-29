# Настройка сервера и маршрутизации
# uvicorn main_01:app --reload аннотация через точку пример uvicorn less05.main_01:app --reload


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
