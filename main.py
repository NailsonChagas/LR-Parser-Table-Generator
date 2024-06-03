from flask import Flask, request, jsonify
from parser_table import *

app = Flask(__name__)


@app.route("/parser/<parser_type>", methods=["POST"])
def handle_post(parser_type):
    productions, terminals, variables = split_productions(
        request.get_json()["productions"]
    )
    first_set = calculate_grammar_first_set(productions, variables)
    
    return jsonify({
        "FIRST": {k: list(v) for k, v in first_set.items()}
    })


if __name__ == "__main__":
    app.run(debug=True)
