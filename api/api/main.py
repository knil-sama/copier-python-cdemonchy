from fastapi import FastAPI
from models.hello_world import HelloWorld

app = FastAPI()


@app.get("/", response_model=HelloWorld)
async def root():
    return HelloWorld(value="Hello World")