from flask import Flask, request, jsonify
from parser_table import *

app = Flask(__name__)

@app.route("/parser/<parser_type>", methods=["POST"])
def handle_post(parser_type):
    productions, terminals, variables = split_productions(request.get_json()["productions"])

    return jsonify({"productions": productions, "terminals": terminals, "variables": variables})

if __name__ == "__main__":
    app.run(debug=True)