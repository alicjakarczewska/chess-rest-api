import flask
import json
from flask import Response
from flaskr.chess import KnightFigure, PawnFigure, KingFigure, QueenFigure, BishopFigure, RookFigure, create_chessboard

app = flask.Flask(__name__)
app.config["DEBUG"] = True

figuresDict = {
        'knight': KnightFigure,
        'pawn': PawnFigure,
        'king': KingFigure,
        'queen': QueenFigure,
        'bishop': BishopFigure,
        'rook': RookFigure
    }

def validate_chess_figure_name(chess_figure):
    message = ""
    if chess_figure.lower() not in figuresDict.keys():
        message = "Figure does not exist."
    return message


def validate_current_field_name(current_field):
    message = ""
    chessboard = create_chessboard()
    if current_field.upper() not in chessboard:
        message = "Field does not exist."
    return message
    

@app.route('/', methods=['GET'])
def home():
    return "<h1>Chess REST API</h1><p>Hello!</p>"


@app.route('/api/v1/<chess_figure>/<current_field>', methods=['GET'])
def get_figure_move_list(chess_figure=None, current_field=None):   

    res = {
        'figure': chess_figure,
        'currentField': current_field
    }

    error_chess_figure = validate_chess_figure_name(chess_figure)
    if error_chess_figure:
        res['availableMoves'] = []
        res['error'] = error_chess_figure
        res_code = 404

        return Response(json.dumps(res),  mimetype='application/json'), res_code

    error_field = validate_current_field_name(current_field)    
    if error_field:
        res['availableMoves'] = []
        res['error'] = error_field
        res_code = 409

        return Response(json.dumps(res),  mimetype='application/json'), res_code
    
    fig = figuresDict[chess_figure.lower()](current_field.upper())
    fig_moves_list = fig.list_available_moves()

    res['availableMoves'] = fig_moves_list
    res['error'] = None
    res_code = 200

    return Response(json.dumps(res),  mimetype='application/json'), res_code

@app.errorhandler(500)
def internal_error(error):
    return "500 error"

app.run()