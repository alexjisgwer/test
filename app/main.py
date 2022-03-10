import flask
from flask import request, jsonify
import re
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
laptops = {"asus":{
    "p2540":{
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    "x56":{
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    "k89":{
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}}
}
def revise(name):
    name=name.strip() ###remove start and end spaces
    name=re.sub(' +', ' ', name) #### remove extra spaces
    name=name.lower()
    return name
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/laptop', methods=['GET'])
def api_id():
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Page Not Found!"
    name=revise(name)
    brand,model=name.split(" ")
    return jsonify([laptops[brand][model]])

@app.route('/search', methods=['GET'])
def api_search():
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Page Not Found!"
    name=revise(name)
    if len(name.split(" "))==1:
        return jsonify(laptops[name])

    brand,model=name.split(" ")
    result=[]
    for laptop in list(laptops[brand].keys()):
        if laptop.startswith(model):
            result.append(laptops[brand][laptop])


    return jsonify(result)
