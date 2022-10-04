import flask
import json
from flask import Response
from flaskr.chess import KnightFigure, PawnFigure, KingFigure, QueenFigure, BishopFigure, RookFigure, create_chessboard

app = flask.Flask(__name__)

chessboard = create_chessboard()

figuresDict = {
        'knight': KnightFigure,
        'pawn': PawnFigure,
        'king': KingFigure,
        'queen': QueenFigure,
        'bishop': BishopFigure,
        'rook': RookFigure
    }

def validate_chess_figure_name(chess_figure):
    res = {}
    if chess_figure.lower() not in figuresDict.keys():
        res['error'] = "Figure does not exist."
        res_code = 404
        return res, res_code
    return None


def validate_field_name(field_name):
    res = {}
    if field_name.upper() not in chessboard:
        res['error'] = "Field does not exist."
        res_code = 409
        return res, res_code
    return None
    

@app.route('/', methods=['GET'])
def home():
    return "<h1>Chess REST API</h1><p>Hello!</p>"


@app.route('/api/v1/<chess_figure>/<current_field>', methods=['GET'])
def get_figure_move_list(chess_figure=None, current_field=None):   

    res = {
        'figure': chess_figure.lower(),
        'currentField': current_field.upper(),
        'availableMoves': [],
        'error': None
    }
    res_code = 200

    err_fig_name = validate_chess_figure_name(chess_figure)
    err_curr_field = validate_field_name(current_field)  

    err = err_fig_name if err_fig_name else False    
    err = err_curr_field if err_curr_field else err

    if err:
        res.update(err[0])
        res_code = err[1]
    else:
        fig = figuresDict[chess_figure.lower()](current_field.upper())
        fig_moves_list = fig.list_available_moves()
        res['availableMoves'] = fig_moves_list

    return Response(json.dumps(res),  mimetype='application/json'), res_code

@app.route('/api/v1/<chess_figure>/<current_field>/<dest_field>', methods=['GET'])
def get_figure_move_validation(chess_figure=None, current_field=None, dest_field=None):   

    res = {
        'figure': chess_figure.lower(),
        'currentField': current_field.upper(),
        'destField': dest_field.upper(),
        'error': None
    }
    res_code = 200

    err_fig_name = validate_chess_figure_name(chess_figure)
    err_curr_field = validate_field_name(current_field)  
    err_dest_field = validate_field_name(dest_field)  

    err = err_fig_name if err_fig_name else False    
    err = err_curr_field if err_curr_field else err
    err = err_dest_field if err_dest_field else err

    if err:
        res.update(err[0])
        res_code = err[1]
    else:
        fig = figuresDict[chess_figure.lower()](current_field.upper())
        answer = fig.validate_move(dest_field.upper())
        res['move'] = 'valid' if answer else 'invalid'            

    return Response(json.dumps(res),  mimetype='application/json'), res_code


@app.errorhandler(500)
def internal_error(error):
    return "500 error"

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)