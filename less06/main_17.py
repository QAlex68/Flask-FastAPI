# Пример 2:

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q:
        results.update({"q": q})
    return results

# В этом примере мы создаем маршрут "/items/" с параметром запроса "q". Параметр
# "q" имеет тип str и должен быть длиной не менее 3 символов. В отличие от первого
# примера, здесь мы используем многоточие (...) в качестве значения по умолчанию
# для параметра "q". Это означает, что параметр "q" обязателен для передачи в
# запросе. Если параметр не передан, то будет сгенерировано исключение.
# Примеры демонстрируют использование fastapi.Query для работы с параметрами
# запроса и проверки строк. При использовании Query мы можем определять
# параметры запроса, задавать для них ограничения на тип данных и значения, а
# также указывать значения по умолчанию.
