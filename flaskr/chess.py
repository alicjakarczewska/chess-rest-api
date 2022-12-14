from abc import ABCMeta
from typing import List


def translate_position_to_list(pos: str) -> List[int]:
    """A function that translating position (string) to list of two ints"""
    pos_list = [ord((pos[0].upper())) - 64, int(pos[1])]
    return pos_list


def translate_list_to_position(pos_list: List[int]) -> str:
    """A function that translating list of two ints to position (string)"""
    pos = chr(pos_list[0] + 64) + str(pos_list[1])
    return pos


def create_chessboard() -> List[str]:
    """A function to create list of chesboard field"""
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    chessboard = []

    for letter in letters:
        for i in range(1, 9):
            chessboard.append(letter + str(i))

    return chessboard


chessboard = create_chessboard()


class Figure(metaclass=ABCMeta):
    def __init__(self, current_field: str):
        if current_field.upper() not in chessboard:
            raise ValueError("invalid argument!")
        self._current_field = translate_position_to_list(current_field)
        self.name = "Figure"

    def __str__(self):
        return self.name

    def list_available_moves(self) -> List[str]:
        X = self._X
        Y = self._Y
        current_field = self._current_field

        pos = []

        for i in range(len(X)):
            x = current_field[0] + X[i]
            y = current_field[1] + Y[i]

            if x > 0 and y > 0 and x <= 8 and y <= 8:
                pos.append(translate_list_to_position([x, y]))

        return pos

    def validate_move(self, dest_field: str) -> bool:
        available_moves_list = self.list_available_moves()
        if dest_field in available_moves_list:
            return True
        else:
            return False


class PawnFigure(Figure):
    def __init__(self, current_field: str, *args, **kwargs):
        super().__init__(current_field)
        self.name = "pawn"
        self._X = [0]
        self._Y = [1]


class KnightFigure(Figure):
    def __init__(self, current_field: str, *args, **kwargs):
        super().__init__(current_field)
        self.name = "knight"
        self._X = [2, 1, -1, -2, -2, -1, 1, 2]
        self._Y = [1, 2, 2, 1, -1, -2, -2, -1]


class BishopFigure(Figure):
    def __init__(self, current_field: str, *args, **kwargs):
        super().__init__(current_field)
        self.name = "bishop"
        self._X = [x for x in range(1, 9)] * 2 + [-x for x in range(1, 9)] * 2
        self._Y = ([x for x in range(1, 9)] + [-x for x in range(1, 9)]) * 2


class RookFigure(Figure):
    def __init__(self, current_field: str, *args, **kwargs):
        super().__init__(current_field)
        self.name = "rook"
        self._X = (
            [x for x in range(1, 9)] + [-x for x in range(1, 9)] + [0] * 16
        )
        self._Y = (
            [0] * 16 + [x for x in range(1, 9)] + [-x for x in range(1, 9)]
        )


class KingFigure(Figure):
    def __init__(self, current_field: str, *args, **kwargs):
        super().__init__(current_field)
        self.name = "king"
        self._X = [0, 1, 1, 1, 0, -1, -1, -1]
        self._Y = [1, 1, 0, -1, -1, -1, 0, 1]


class QueenFigure(Figure):
    def __init__(self, current_field: str, *args, **kwargs):
        super().__init__(current_field)
        self.name = "queen"

    def list_available_moves(self) -> List[str]:
        position = translate_list_to_position(self._current_field)

        rook_figure = RookFigure(position)
        bishop_figure = BishopFigure(position)

        pos_rook = rook_figure.list_available_moves()
        pos_bishop = bishop_figure.list_available_moves()
        pos = pos_bishop + pos_rook

        return pos
