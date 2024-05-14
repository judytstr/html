from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def stronaglowna():
    return render_template('stronaglowna.html')

@app.route('/historia/')
def historia():
    return render_template('historia.html')

if __name__ == "__main__":
    app.run(debug=True)