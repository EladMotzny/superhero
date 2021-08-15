import requests
from flask import Flask, render_template, request, redirect
from backend.models import Hero
from backend.api import search_hero

# initialize the app
app = Flask(__name__)


#Will save the list of the previously searched superheroes
previous_heroes = []

@app.route('/')
def home():
    return render_template('index.html', heroes = previous_heroes)

@app.route('/search', methods = ['GET','POST'])
def search():
    if request.method == 'POST':
        hero = search_hero(request.form['search'])
        previous_heroes.insert(0,hero)
        return redirect('/')
    else:
        return render_template('index.html', heroes = previous_heroes)


if __name__ == "__main__":
    app.run(debug=True)

