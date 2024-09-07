
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

from fastapi.responses import HTMLResponse
app = FastAPI()

class Item(BaseModel):
    name: str
    price: str

class HealthCondition(BaseModel):
    condition: str
    age: int

class HondaStore(BaseModel):
    model: str
    year: int

class HondaSpecs(BaseModel):
    cc: int
    fuel: str

# Routes
@app.get("/balaji",response_class=HTMLResponse)
def balaji():
    return """
    <HTML>
        <head>
            <title>some HTML in here</title>
        </head>
        <body>
            <h1>look ma! HTML!</h1>
            <h2>arivu anna </h2>
            <h3>abi machi </h3>
        </body>
    </html>
    """

@app.get("/abi")
def read_abi():
    return {"abi machiiii"}

@app.get("/python")
def read_python():
    return {"my main py"}

@app.get("/variables")
def can():
    return {"this is the two variables"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.post("/alagammal")
async def create_alagammal(health: HealthCondition):
    return {"condition": health.condition, "age": health.age}

@app.post("/balaji_health")
async def create_balaji_health(health: HealthCondition):
    return {"condition": health.condition, "age": health.age}

@app.post("/honda_store")
async def create_honda_store(honda: HondaStore):
    return {"model": honda.model, "year": honda.year}

@app.post("/honda_specs")
async def create_honda_specs(honda: HondaSpecs):
    return {"cc": honda.cc, "fuel": honda.fuel}

@app.post("/ktm_store")
async def create_honda_store(ktm: HondaStore):
    return {"model": ktm.model,"year":ktm.year}

@app.get("/",response_class=HTMLResponse)
def home():
    return """
    <HTML>
        <head>
            <title>some HTML in here</title>
        </head>
        <body>
            <h1>look ma! HTML!</h1>
            <h2>arivu anna </h2>
            <h3>abi machi </h3>
        </body>
    </html>
    """

@app.get("/balaji/")
async def read_balaji():
    html_content="""
    <html>
        <head>
            <title> text-align:center
            some HTML IN HERE</title>
        </head>
        <body>
            div .a{
                    text-align:center;
                }
            <h1>look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

