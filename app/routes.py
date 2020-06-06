from app import app
from flask import render_template, flash, redirect, url_for, make_response, jsonify, abort, request
import yaml
from yaml import load, dump, Loader
import json

poke = None
stream = None
url = 'http://127.0.0.1:5000/'

def Load():
    global poke, stream
    stream = open('app/db/pokemony.yaml', 'r')
    poke = yaml.load(stream, Loader=yaml.FullLoader)
    stream.close()

def Save():
    global poke, stream
    stream = open('app/db/pokemony.yaml', 'w')
    stream.write(yaml.dump(poke,default_flow_style=False))
    stream.close()

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error':'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}), 404)

@app.errorhandler(500)
def interna_server_error(error):
    return make_response(jsonify({'error':'Internal Server Error'}), 500)

@app.errorhandler(409)
def conflict(error):
    return make_response(jsonify({'error': 'Conflict'}), 409)

@app.route('/')

@app.route('/index')
def index():
    return make_response(render_template('index.html', title='Glowna'), 200)

@app.route('/pokemon/<string:id>', methods = ['GET'])
def get_pokemon(id):
    try:
        Load()
        return jsonify({id : json.dumps(poke['pokemon'][id])}),200
    except KeyError:
        abort(400)
    
@app.route('/pokemon/<string:id>', methods = ['POST'])
def add_pokemon(id):
    global poke
    if not request.json:
        abort(400)
    else:
        Load()
        temp = dict(**{'pokemon' : {id: request.json}})
        temp2 = poke
        for i in temp['pokemon']:
            temp2['pokemon'].update({i:temp['pokemon'][i]})
        poke = temp2
        Save()
        return make_response(jsonify({'url' : url + 'pokemon/'+id}),201)

@app.route('/pokemon/<string:id>', methods = ['DELETE'])
def delete_pokemon(id):
    try:
        Load()
        del poke ['pokemon'][id]
        Save()
        return make_response(' ', 204)
    except KeyError:
        return abort(409)

@app.route('/pokemon/<string:id>', methods = ['PUT'])
def mod_pokemon(id):
    global poke
    try:
        if not request.json:
            abort(400)
        else:
            Load()
            del poke ['pokemon'][id]
            Save()
            Load()
            temp = dict(**{'pokemon' : {id : request.json}})
            temp2 = poke
            for i in temp['pokemon']:
                temp2['pokemon'].update({i : temp['pokemon'][i]})
            poke = temp2
            Save()
            return make_response(jsonify({'url' : url + 'pokemon/'+id}),201)
    except KeyError:
        return abort(409)
