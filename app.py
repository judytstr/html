from flask import Flask, render_template, request

app = Flask(__name__)

history = []

@app.route('/')
def stronaglowna():
    current_balance = 1000  # Przykładowe saldo
    current_inventory = {'Produkt A': 10, 'Produkt B': 20, 'Produkt C': 15}  # Przykładowy magazyn
    return render_template('stronaglowna.html', balance=current_balance, inventory=current_inventory)

@app.route('/historia/')
@app.route('/historia/<int:line_from>/<int:line_to>/')
def historia(line_from=None, line_to=None):
    if line_from is None or line_to is None:
        return render_template('historia.html', history=history)
    else:
        return render_template('historia.html', history=history[line_from:line_to])

if __name__ == "__main__":
    app.run(debug=True)

