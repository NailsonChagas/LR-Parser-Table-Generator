from flask import Flask, request, jsonify
from parser_table import *

app = Flask(__name__)

@app.route("/parser/<parser_type>", methods=["POST"])
def handle_post(parser_type):
    productions, terminals, variables = split_productions(request.get_json()["productions"])
    first_set = calculate_first(productions, terminals, variables)
    follow_set = calculate_follow(productions, first_set, variables)
    
    return jsonify({
        "FIRST": first_set,
        "FOLLOW": follow_set
    })

if __name__ == "__main__":
    app.run(debug=True)