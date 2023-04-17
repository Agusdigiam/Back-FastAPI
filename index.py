from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get('/')
def read_root():
    return{"Backend": "Funcionando en Python"}