# Настройка FastAPI - Запуск приложения
# pip install fastapi
# pip install "uvicorn[standard]"
# uvicorn main_01:app --reload аннотация через точку пример uvicorn less05.main_01:app --reload


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
