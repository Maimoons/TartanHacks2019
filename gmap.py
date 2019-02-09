'''
A Web application that shows Google Maps around schools, using
the Flask framework, and the Google Maps API.
'''

from flask import Flask, render_template, abort
app = Flask(__name__)


class Person:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

people = (
    Person('dennisy',      'Dennis Yu',    40.4426978, -79.944708),
    Person('Mamoons', 'Maria Moons',       40.4419296, -79.9428409),
    Person('wobald',     'Wally Bald',     40.4425345, -79.9461885)
)
people_by_key = {person.key: person for person in people}


@app.route("/")
def index():
    return render_template('index.html', people=people)


@app.route("/<person_code>")
def show_person(person_code):
    person = people_by_key.get(person_code)
    if person:
        return render_template('map.html', person=person)
    else:
        abort(404)

app.run(host='localhost', debug=True)
