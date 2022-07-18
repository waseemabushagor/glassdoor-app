from flask import Flask
from flask import jsonify
from python_library.tech_companies_json import json_dic

app = Flask(__name__)

list_of_company_dict = json_dic["companies"]

@app.route('/')
def hello():
    return 'Hello World! I can make search route: /search/'

@app.route('/search/<location>')
def search_location(location):
    for i in range(len(list_of_company_dict)):
        location_value = list_of_company_dict[i]["country"]
        if location or location.lower() == location_value:
            print(list_of_company_dict[i])
        elif location or location.lower() == "USA":
            print(list_of_company_dict[i])

@app.route('/search/<rank>')
def search_rank(rank):
    for i in range(len(list_of_company_dict)):
        rank_value = list_of_company_dict[i]["Rank"]
        if rank == rank_value:
            return list_of_company_dict[i]

@app.route('/search/<symbol>')
def search_symbol(symbol):
    for i in range(len(list_of_company_dict)):
        symbol_value = list_of_company_dict[i]["Symbol"]
        if symbol.upper() == symbol_value:
            return list_of_company_dict[i]

@app.route('/search/<marketcap>')
def search_marketcap_lessthan(marketcap):
    for i in range(len(list_of_company_dict)):
        marketcap_value = list_of_company_dict[i]["marketcap"]
        if marketcap >= marketcap_value:
            print(list_of_company_dict[i])

@app.route('/search/<name>')
def search_name(name):
    for i in range(len(list_of_company_dict)):
        name_value = list_of_company_dict[i]['Name']
        if name or name.lower() == name_value:
            return list_of_company_dict[i]


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
