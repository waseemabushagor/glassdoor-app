from fastapi import FastAPI
import uvicorn
import python_library.tech_companies_json
from python_library.tech_companies_json import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API.  Call /search"}


@app.get("/search/{name}")
async def search(value: str):
    """Search by company name"""

    result = search_name(name)
    return {"result": result}

@app.get("/search/{location}")
async def search_location(value: str):
    """Search by company location"""

    result = search_location(location)
    return {"result": result}

@app.get("/search/{symbol}")
async def search_symbol(value: str):
    """Search by company stock symbol"""

    result = search_symbol(symbol)
    return {"result": result}

@app.get("/search/{rank}")
async def search_rank(value: int):
    """Search by company marketcap rank"""

    result = search_rank(rank)
    return {"result": result}

@app.get("/search/{marketcap}")
async def search(value: int):
    """Search for companies marketcap less than the entered amount"""

    result = search_marketcap_lessthan(marketcap)
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")