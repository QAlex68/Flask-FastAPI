from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item"), q: str = None):
    return {"item_id": item_id, "q": q}

# В этом примере мы создаем маршрут "/items/{item_id}" с параметром пути "item_id".
# Кроме ограничений на тип данных и значения, мы также задаем для параметра
# "item_id" заголовок "The ID of the item". Это заголовок будет использоваться при
# генерации документации API: http://127.0.0.1:8000/redoc.
# Примеры демонстрируют использование fastapi.Path для работы с параметрами
# пути и проверки данных. При использовании Path мы можем определять параметры
# пути, задавать для них ограничения на тип данных и значения, а также указывать
# заголовки для документации API.