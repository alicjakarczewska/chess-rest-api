from app import app

def test_index_route():
    response = app.test_client().get('/')

    assert response.status_code == 200
  
def test_get_move_list_route():
    response = app.test_client().get('/api/v1/king/h2')

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'figure', 'currentField', 'availableMoves', 'error'}
    assert response.json['figure'] == 'king'
    assert response.json['currentField'] == 'H2'
    assert response.json['availableMoves'] == ["H3", "H1", "G1", "G2", "G3"]
    assert response.json['error'] == None

def test_get_move_list_with_incorrect_figure_name_route():
    response = app.test_client().get('/api/v1/kings/h2')

    assert response.status_code == 404
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'figure', 'currentField', 'availableMoves', 'error'}
    assert response.json['figure'] == 'kings'
    assert response.json['currentField'] == 'H2'
    assert response.json['availableMoves'] == []
    assert response.json['error'] == "Figure does not exist."

def test_get_move_list_with_incorrect_field_name_route():
    response = app.test_client().get('/api/v1/king/h9')

    assert response.status_code == 409
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'figure', 'currentField', 'availableMoves', 'error'}
    assert response.json['figure'] == 'king'
    assert response.json['currentField'] == 'H9'
    assert response.json['availableMoves'] == []
    assert response.json['error'] == "Field does not exist."

def test_validate_valid_move_route():
    response = app.test_client().get('/api/v1/king/h2/h3')

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'figure', 'currentField', 'destField', 'error', 'move'}
    assert response.json['figure'] == 'king'
    assert response.json['currentField'] == 'H2'
    assert response.json['destField'] == 'H3'
    assert response.json['error'] == None
    assert response.json['move'] == 'valid'

def test_validate_invalid_move_route():
    response = app.test_client().get('/api/v1/king/h2/h4')

    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'figure', 'currentField', 'destField', 'error', 'move'}
    assert response.json['figure'] == 'king'
    assert response.json['currentField'] == 'H2'
    assert response.json['destField'] == 'H4'
    assert response.json['error'] == None
    assert response.json['move'] == 'invalid'


def test_validate_move_with_incorrect_curr_field_name_route():
    response = app.test_client().get('/api/v1/king/h9/h4')

    assert response.status_code == 409
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'figure', 'currentField', 'destField', 'error'}
    assert response.json['figure'] == 'king'
    assert response.json['currentField'] == 'H9'
    assert response.json['destField'] == 'H4'
    assert response.json['error'] == "Field does not exist."

def test_validate_move_with_incorrect_dest_field_name_route():
    response = app.test_client().get('/api/v1/king/h4/h9')

    assert response.status_code == 409
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) >= {'figure', 'currentField', 'destField', 'error'}
    assert response.json['figure'] == 'king'
    assert response.json['currentField'] == 'H4'
    assert response.json['destField'] == 'H9'
    assert response.json['error'] == "Field does not exist."

def test_validate_move_with_incorrect_figure_name_route():
  response = app.test_client().get('/api/v1/kings/h4/h3')

  assert response.status_code == 404
  assert response.content_type == 'application/json'
  assert isinstance(response.json, dict)
  assert set(response.json.keys()) >= {'figure', 'currentField', 'destField', 'error'}
  assert response.json['figure'] == 'kings'
  assert response.json['currentField'] == 'H4'
  assert response.json['destField'] == 'H3'
  assert response.json['error'] == "Figure does not exist."