from fastapi import FastAPI
import random
import httpx
import requests
from fastapi.logger import logger
from pydantic import BaseModel
from typing import Optional


app=FastAPI()
 

@app.get('/')
async def home():
    logger.warning("This is a warning message")
    return 'Hello world'

# Path Param 
@app.get('/welcome/{name}')
def welcome(name:str):
    return f'{name} welcome to Out app'

# Query Param or Request Param Demo
@app.get('/random')
def getRandom(range:int):
    return random.randint(0,range)

# Request Body
class Item(BaseModel):
    name:str
    description:Optional[str]=None
    price:float

@app.post('/saveItem')
async def saveItem(item:Item):
    return f'item with name {item.name} created'


@app.get("/asyn")
async def asyn():
    # Simulate fetching data from an external API asynchronously
    logger.warning("fetching data with async")
    async with httpx.AsyncClient() as client:
        response = await client.get("https://reqres.in/api/users?delay=3")
        data = response.json()
    logger.warning("fetched data with async")
    return {"data": data}

@app.get('/wait')
def wait():
    logger.warning("fetching data without async")
    url = "https://reqres.in/api/users?delay=3"
    response = requests.get(url)

    if response.status_code == 200:
        logger.warning("fetched data without async")
        data = response.json()
        return {"data": data}
    else:
        return {"data": data}



