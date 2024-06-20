from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/partidos')
def partidos():
    return render_template('partidos.html')

@app.route('/contacto')
def contacto():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

