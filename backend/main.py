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




@app.route("/getcode", methods= ['POST', 'GET'])
def get_code():
   
    
    data = request.json
    
    code = data.get("text")
    tree , compiled_answer = compile(code)
    answer = {
        
        "compiled_answer": compiled_answer
        }
    
    return jsonify(answer) 




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