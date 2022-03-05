from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc', #aby przegladarka korzystala z sesji
))
 
# lista pytań
DANE = [{
    'pytanie': 'Stolica Hiszpani, to:',  # pytanie
    'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],  # możliwe odpowiedzi
    'odpok': 'Madryt'},  # poprawna odpowiedź
    {
    'pytanie': 'Objętość sześcianu o boku 6 cm, wynosi:',
    'odpowiedzi': ['36', '216', '18'],
    'odpok': '216'},
    {
    'pytanie': 'Symbol pierwiastka Helu, to:',
    'odpowiedzi': ['Fe', 'H', 'He'],
    'odpok': 'He'},
]

#@app.route("/")  #@-dekorator kod ktory wykona sie przed 
@app.route("/", methods = {"GET", "POST"})  #@-dekorator kod ktory wykona sie przed 
def quiz():
    #return "<p>Hello, World!</p>"
    #return render_template("index.html")
    if request.method == "POST":
        punkty=0
        odpowiedzi = request.form

        for nr_pytania, odpowiedz in odpowiedzi.items():
            if odpowiedz == DANE[int(nr_pytania)]["odpok"]:
                punkty = punkty +1
        flash("Liczba poprawnych odpowiedzi, to: {}".format(punkty))
        return redirect(url_for("quiz"))


    return render_template("index.html",pytania = DANE)
if __name__ == "__main__":
    app.run(debug = True)