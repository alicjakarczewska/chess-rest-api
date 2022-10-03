import flask
import json
from flask import Response
from flaskr.chess import KnightFigure 

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Chess REST API</h1><p>Hello!</p>"

@app.route('/api/v1/<chess_figure>/<current_field>')
def get_figure_move_list(chess_figure=None, current_field=None):
    
    k = KnightFigure('A1')
    k_list = k.list_available_moves()


    js = [ { "moves" : k_list, "name" : k.name} ]
    return Response(json.dumps(js),  mimetype='application/json')


app.run()