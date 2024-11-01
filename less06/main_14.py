# Больше про валидацию данных
# Ранее мы рассматривали возможность указать тип для переменной, чтобы FastAPI
# сделал проверку данных по типу. В начале лекции поговорили о модели данных и
# возможностях pydantic.Field для валидации полей модели. Рассмотрим работу с
# fastapi.Path и fastapi.Query
# Проверка параметра пути через Path
# fastapi.Path — это класс, который используется для работы с параметрами пути
# (path parameters) в URL и проверки данных. Он позволяет определять параметры
# пути, которые будут передаваться в URL, а также задавать для них ограничения на
# тип данных и значения.

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., ge=1), q: str = None):
    return {"item_id": item_id, "q": q}

# В этом примере мы создаем маршрут "/items/{item_id}" с параметром пути "item_id".
# Параметр "item_id" имеет тип int и должен быть больше или равен 1. Мы используем
# многоточие (...) в качестве значения по умолчанию для параметра "item_id", что
# означает, что параметр обязателен для передачи в URL. Если параметр не передан
# или его значение меньше 1, то будет сгенерировано исключение.
