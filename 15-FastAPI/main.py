from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.counter = 0


class Product(BaseModel):
    name: str
    desc: Optional[str] = None
    price: float
    code: str
    tax: Optional[float] = None



class HelloResp(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

"""
@app.get("/hello/{name}")
def hello_name(name: str):
    return f'Hello {name.capitalize()}'

"""


@app.get("/counter")
def count():
    app.counter +=1
    return {"counter = ": app.counter}


@app.get("/hello/{name}", response_model=HelloResp)
def hello_name_view(name: str):
    return HelloResp(msg=f"Hello {name}")


@app.post("/products")
def create_product(prod: Product):
    #save to data
    return prod
