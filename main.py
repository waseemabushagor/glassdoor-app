from flask import Flask
from flask import jsonify
from tech_companies_json import new_list_of_company_dict

app = Flask(__name__)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return "Hello World! I can search at route: /search"


@app.route("/name/<name>")
def search_name(name):
    for i in range(len(new_list_of_company_dict)):
        name_value = new_list_of_company_dict[i]["Name"]
        if name == name_value or "".join(name_value.split()).lower():
            return jsonify(new_list_of_company_dict[i])


@app.route("/symbol/<symbol>")
def search_symbol(symbol):
    for i in range(len(new_list_of_company_dict)):
        symbol_value = new_list_of_company_dict[i]["Symbol"]
        if symbol.upper() == symbol_value:
            return jsonify(new_list_of_company_dict[i])


@app.route("/rank/<rank>")
def search_rank(rank):
    for i in range(len(new_list_of_company_dict)):
        rank_value = new_list_of_company_dict[i]["Rank"]
        if int(rank) == rank_value:
            return jsonify(new_list_of_company_dict[i])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
