# Автоматическая документация по API - Интерактивная документация Swagger - Альтернативная документация ReDoc
# http://localhost:8000/docs
# http://localhost:8000/redoc
# Схема - меняет заголовки и другую информацию для docs и redoc - http://localhost:8000/api/v1/openapi.json адрес схемы


from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(openapi_url="/api/v1/openapi.json")


@app.get("/hello/{name}")
async def read_item(name: str, age: int):
    return {"Hello": name, "Age": age}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title MYMY",
        version="1.0.0",
        description="This is a very custom OpenAPI schema blabla",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
