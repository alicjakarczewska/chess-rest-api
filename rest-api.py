import flask
import json
from flask import Response
from flaskr.chess import KnightFigure, PawnFigure, KingFigure, QueenFigure, BishopFigure, RookFigure

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Chess REST API</h1><p>Hello!</p>"

@app.route('/api/v1/<chess_figure>/<current_field>')
def get_figure_move_list(chess_figure=None, current_field=None):
    
    functionsDict = {
        'knight': KnightFigure,
        'pawn': PawnFigure,
        'king': KingFigure,
        'queen': QueenFigure,
        'bishop': BishopFigure,
        'rook': RookFigure
    }

    # validate_chess_figure_name(chess_figure)

    # validate_current_field_name(current_field)

    fig = functionsDict[chess_figure](current_field)
    fig_moves_list = fig.list_available_moves()

    js = [ { "moves" : fig_moves_list, "name" : fig.name} ]
    return Response(json.dumps(js),  mimetype='application/json')


app.run()