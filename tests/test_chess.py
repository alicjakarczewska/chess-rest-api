from flaskr.chess import (
    KnightFigure,
    PawnFigure,
    KingFigure,
    QueenFigure,
    BishopFigure,
    RookFigure,
    create_chessboard,
    translate_list_to_position,
    translate_position_to_list,
)
import collections
import pytest

# Tests for creating figures objects
def test_knight_create():
    fig = KnightFigure("A5")
    assert fig.name == "knight"


def test_king_create():
    fig = KingFigure("A5")
    assert fig.name == "king"


def test_rook_create():
    fig = RookFigure("A5")
    assert fig.name == "rook"


def test_pawn_create():
    fig = PawnFigure("A5")
    assert fig.name == "pawn"


def test_bishop_create():
    fig = BishopFigure("A5")
    assert fig.name == "bishop"


def test_queen_create():
    fig = QueenFigure("A5")
    assert fig.name == "queen"


# Test for creating a figure object with invalid argument current_field
def test_create_figure_with_invalid_current_field_arg():
    with pytest.raises(ValueError, match="invalid argument!"):
        fig = KnightFigure("A55")


# Tests for list figures available moves
def test_knight_list_available_moves():
    fig = KnightFigure("A5")
    actual = fig.list_available_moves()
    expected = ["C4", "B7", "B3", "C6"]
    assert collections.Counter(actual) == collections.Counter(expected)


def test_king_list_available_moves():
    fig = KingFigure("A5")
    actual = fig.list_available_moves()
    expected = ["A6", "B6", "B5", "B4", "A4"]
    assert collections.Counter(actual) == collections.Counter(expected)


def test_rook_list_available_moves():
    fig = RookFigure("A5")
    actual = fig.list_available_moves()
    expected = [
        "B5",
        "C5",
        "D5",
        "E5",
        "F5",
        "G5",
        "H5",
        "A6",
        "A7",
        "A8",
        "A4",
        "A3",
        "A2",
        "A1",
    ]
    assert collections.Counter(actual) == collections.Counter(expected)


def test_pawn_list_available_moves():
    fig = PawnFigure("A5")
    actual = fig.list_available_moves()
    expected = ["A6"]
    assert collections.Counter(actual) == collections.Counter(expected)


def test_bishop_list_available_moves():
    fig = BishopFigure("A5")
    actual = fig.list_available_moves()
    expected = ["B6", "C7", "D8", "B4", "C3", "D2", "E1"]
    assert collections.Counter(actual) == collections.Counter(expected)


def test_queen_list_available_moves():
    fig = QueenFigure("A5")
    actual = fig.list_available_moves()
    expected = [
        "B6",
        "C7",
        "D8",
        "B4",
        "C3",
        "D2",
        "E1",
        "B5",
        "C5",
        "D5",
        "E5",
        "F5",
        "G5",
        "H5",
        "A6",
        "A7",
        "A8",
        "A4",
        "A3",
        "A2",
        "A1",
    ]
    assert collections.Counter(actual) == collections.Counter(expected)


# Tests for figures moves validation


def test_knight_validate_move():
    fig = KnightFigure("A5")
    valid_move = fig.validate_move("C6")
    invalid_move = fig.validate_move("C7")
    assert valid_move == True
    assert invalid_move == False


def test_king_validate_move():
    fig = KingFigure("A5")
    valid_move = fig.validate_move("A6")
    invalid_move = fig.validate_move("C7")
    assert valid_move == True
    assert invalid_move == False


def test_rook_validate_move():
    fig = RookFigure("A5")
    valid_move = fig.validate_move("B5")
    invalid_move = fig.validate_move("C7")
    assert valid_move == True
    assert invalid_move == False


def test_pawn_validate_move():
    fig = PawnFigure("A5")
    valid_move = fig.validate_move("A6")
    invalid_move = fig.validate_move("C7")
    assert valid_move == True
    assert invalid_move == False


def test_bishop_validate_move():
    fig = BishopFigure("A5")
    valid_move = fig.validate_move("B6")
    invalid_move = fig.validate_move("C6")
    assert valid_move == True
    assert invalid_move == False


def test_queen_validate_move():
    fig = QueenFigure("A5")
    valid_move = fig.validate_move("B6")
    invalid_move = fig.validate_move("B7")
    assert valid_move == True
    assert invalid_move == False


# test position translation function


def test_translate_position_to_list():
    actual = translate_position_to_list("B5")
    expected = [2, 5]
    assert actual == expected


def test_translate_list_to_position():
    actual = translate_list_to_position([2, 5])
    expected = "B5"
    assert actual == expected


def test_create_chessboard():
    actual = create_chessboard()

    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    expected = []
    for l in letters:
        for i in range(1, 9):
            expected.append(l + str(i))

    assert actual == expected
