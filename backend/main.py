from flask import Flask

app = Flask(__name__)

@app.route("/tree", methods= ["post"])
def home():
    return "Hello, World!"
@app.route("/table", methods= ["post"])
def home():
    return "Hello, World!"    
if __name__ == "__main__":
    app.run(debug=True)