from fastapi import FastAPI
import uvicorn
from python_library.tech_companies_json import *

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API.  Call /search"}


@app.get("/search/{name}")
def search_name(value: str):
    """search by company name"""
    result = search_name(name)
    return {"result": result}


@app.get("/search/{location}")
def search_location(value: str):
    """Search by company location"""
    result = search_location(location)
    return {"result": result}


@app.get("/search/{symbol}")
def search_symbol(value: str):
    """Search by company stock symbol"""

    result = search_symbol(symbol)
    return {"result": result}


@app.get("/search/{rank}"):
def search_rank(value: int):
    """Search by company marketcap rank"""

    result = search_rank(rank)
    return {"result": result}


@app.get("/search/{marketcap}")
def search_marketcap_lessthan(value: int):
    """Search for companies marketcap less than the entered amount"""

    result = search_marketcap_lessthan(marketcap)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
