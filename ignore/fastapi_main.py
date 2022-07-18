from fastapi import FastAPI
import uvicorn
from python_library.tech_companies_json import search_location, search_name, search_rank, search_marketcap_lessthan, search_symbol

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API.  Call /search"}


@app.get("/search/{name}")
    """search by company name"""
    
    result = search_name(name)
    return {"result": result}


@app.get("/search/{location}")
    """Search by company location"""
    result = search_location(location)
    return {"result": result}


@app.get("/search/{symbol}")
    """Search by company stock symbol"""

    result = search_symbol(symbol)
    return {"result": result}


@app.get("/search/{rank}")
    """Search by company marketcap rank"""

    result = search_rank(rank)
    return {"result": result}


@app.get("/search/{marketcap}")
    """Search for companies marketcap less than the entered amount"""

    result = search_marketcap_lessthan(marketcap)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
