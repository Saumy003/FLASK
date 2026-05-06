# general basic syntax

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='color:green'> Hello World...Something else </h1>"

@app.route("/about")
def about():
    return "This is about section..."

if __name__=="__main__":
    app.run(debug=True)