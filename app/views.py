from flask import render_template
from app import app
from .request import get_articles

@app.route('/') #localhost:5000
def index():
    health_articles = get_articles('health')
    return render_template('index.html',health = health_articles)