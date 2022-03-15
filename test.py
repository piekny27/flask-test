from fileinput import filename
from flask import Flask, current_app, url_for, request
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

#url_for?????????????????
@app.route("/calculate<int:variableA><string:operation><int:variableB>")
def calculate(operation,variableA, variableB):
    wynik=0
    if operation == "add":
        wynik = variableA+variableB
    elif operation == "subtract":
        wynik = variableA-variableB
    elif operation == "multiply":
        wynik = variableA*variableB
    else:
        return "Błędne działanie"
    return f"Wynik {operation} wynosi: {wynik}"

@app.route('/users/<username>')
def profile(username):
    return f"{username}\'s profile"

with app.test_request_context(): #potrzebne do testowania url_for
    #url_for zwraca app.route wywołanej funkcji z parametrami np. profile lub login
    #ale po co to ja nie wiem edit:już wiem
    print(url_for('profile', username='John Doe'))
    print(url_for("calculate", operation="add", variableA=333, variableB=555))

#????????????????????????

#metody HTTP
@app.route("/methods", methods=["GET","POST"]) #HEAD, PUT,DELETE,OPTIONS, TRACE, CONNECT, PATCH
def methods():
    if request.method == "POST":
        return "Metoda POST"
    else:
        return "Metoda GET"

#pliki statyczne
with app.test_request_context():
    print(url_for("static",filename="cloud01.png"))

#szablony renderowania
