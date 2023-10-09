from flask import Flask,request, jsonify, session
import requests
from flask_cors import CORS
import json
import sys
 

sys.path.insert(1, './compiler')
from symbol_table import *
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure secret key
CORS(app)




@app.route("/getcode", methods=['POST', 'GET'])
def get_code():
    data = request.json
    code = data.get("text")

    # Compile the code and get the result tuple containing formatted_tree, symbol_table, and mips_assembly
    result = compile(code)

    # Return the result as a JSON response
    response = {
        "formatted_tree": result[0],
        "symbol_table": result[1],
        "mips_assembly": result[2]
    }

    return jsonify(response)





@app.route("/compile", methods= ["get"])
def compile_code():
    stored_data = session.get('data', None)
    print(stored_data)
    # code = json.loads(data)
    # print(code)
    # compiled_answer = compile(code)
    # print(compiled_answer)
    # print(code)
    return jsonify({"compiled_answer": "compiled_answer"})
    
       
if __name__ == "__main__":
    app.run(debug=True)