from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def dashboard():
    return render_template('index.html')

#Component
@app.route('/components-alerts.html')
def components_alerts():
    return render_template('components-alerts.html')

@app.route('/components-accordion.html')
def components_accordion():
    return render_template('components-accordion.html')

@app.route('/components-badges.html')
def components_badges():
    return render_template('components-badges.html')


if __name__ == '__main__':
    app.run(debug=True)