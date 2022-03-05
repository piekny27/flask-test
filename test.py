from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#przechwytywanie wartosci z URL i wykorzystanie jako zmiennej w funkcji:
@app.route("/user/<string:name>") #string/int/float/path/uuid
def hello(name):
    name = "[USER] " + name
    return f"Hello, {escape(name)}!" #protect from injection &, <, >, ', and ” in string to HTML-safe sequences
    #return f"Hello, {name}!" #dziala ale jest niezabezpieczone

@app.route("/index")
def index():
    return "<p>Index</p>"

@app.route("/projects/") #końcowy ukośnik określający dalsze podkatalogi
def projects():
    return "Projects:"

#url_for????