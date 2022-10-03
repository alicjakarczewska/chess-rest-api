from abc import ABCMeta

def translate_position_to_list(pos):
    """A function that translating position (string) to list of two ints"""
    pos_list = [ord((pos[0].upper()))-64, int(pos[1])]
    return pos_list


def translate_list_to_position(pos_list):
    """A function that translating list of two ints to position (string)"""
    pos = chr(pos_list[0]+64) + str(pos_list[1])
    return pos


class Figure(metaclass=ABCMeta):

    def __init__(self, current_field=None):
      self._current_field = current_field
      self.name = 'Figure'

    def __str__(self):
      return self.name
    
    def list_available_moves(self, *args, **kwargs):
      pass

    def validate_move(dest_field):
      logger.info("Not implemented")

    def get_available_moves(self):

        X = self._X
        Y = self._Y
        current_field = self._current_field

        pos = []

        for i in range(len(X)):
          x = current_field[0] + X[i]
          y = current_field[1] + Y[i]
          
          if(x > 0 and y > 0 and x <= 8 and y <= 8):
            pos.append(translate_list_to_position([x, y]))

        return pos


class PawnFigure(Figure):

    def __init__(self, current_field=None, *args, **kwargs):
        super().__init__(current_field)
        self.name = 'pawn'
        self._X = [0]
        self._Y = [1]

    def list_available_moves(self):
        pos = self.get_available_moves()
        return pos

class KnightFigure(Figure):

    def __init__(self, current_field=None, *args, **kwargs):
        super().__init__(current_field)
        self.name = 'knight'
        self._X = [2, 1, -1, -2, -2, -1, 1, 2]
        self._Y = [1, 2, 2, 1, -1, -2, -2, -1]

    def list_available_moves(self):
        pos = self.get_available_moves()
        return pos


class BishopFigure(Figure):

    def __init__(self, current_field=None, *args, **kwargs):
        super().__init__(current_field)
        self.name = 'bishop'
        self._X = [x for x in range(1,9)] * 2 + [-x for x in range(1,9)] * 2
        self._Y = ([x for x in range(1,9)] + [-x for x in range(1,9)]) * 2

    def list_available_moves(self):
        pos = self.get_available_moves()
        return pos


class RookFigure(Figure):

    def __init__(self, current_field=None, *args, **kwargs):
        super().__init__(current_field)
        self.name = 'rook'
        self._X = [x for x in range(1,9)] + [-x for x in range(1,9)] + [0] * 16
        self._Y = [0] * 16 + [x for x in range(1,9)] + [-x for x in range(1,9)]

    def list_available_moves(self):
        pos = self.get_available_moves()
        return pos


class QueenFigure(Figure):

    def __init__(self, current_field=None, *args, **kwargs):
        super().__init__(current_field)
        self.name = 'queen'

    def list_available_moves(self):
        rook_figure = RookFigure(self._current_field)
        bishop_figure = BishopFigure(self._current_field)

        pos_rook = rook_figure.get_available_moves()
        pos_bishop = bishop_figure.get_available_moves()
        pos = pos_bishop + pos_rook

        return pos


class KingFigure(Figure):

    def __init__(self, current_field=None, *args, **kwargs):
        super().__init__(current_field)
        self.name = 'king'
        self._X = [0, 1, 1, 1, 0, -1, -1, -1]
        self._Y = [1, 1, 0, -1, -1, -1, 0, 1]

    def list_available_moves(self):
        pos = self.get_available_moves()
        return pos

# Driver code
if __name__ == '__main__':

    k_position = translate_position_to_list("A8")

    k = QueenFigure(k_position)
    print(k.name, k.list_available_moves())

    k = RookFigure(k_position)
    print(k.name, k.list_available_moves())

    k = KnightFigure(k_position)
    print(k.name, k.list_available_moves())

    k = BishopFigure(k_position)
    print(k.name, k.list_available_moves())

    k = KingFigure(k_position)
    print(k.name, k.list_available_moves())

    k = PawnFigure(k_position)
    print(k.name, k.list_available_moves())