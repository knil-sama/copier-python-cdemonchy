from fastapi import FastAPI
from models import HelloWorld

app = FastAPI()


@app.get("/", response_model=HelloWorld)
async def root():
    return HelloWorld("Hello World")