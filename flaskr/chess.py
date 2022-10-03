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


    def list_available_moves(self, *args, **kwargs):
      pos = get_available_moves(self)
      return pos

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


class KnightFigure(Figure):

    def __init__(self, current_field=None, *args, **kwargs):
        super().__init__(current_field)
        self._X = [2, 1, -1, -2, -2, -1, 1, 2]
        self._Y = [1, 2, 2, 1, -1, -2, -2, -1]

    def list_available_moves(self):
        pos = self.get_available_moves()
        return pos


# Driver code
if __name__ == '__main__':

    k_position = "H5"

    k = KnightFigure(translate_position_to_list(k_position))
    k_pos = k.list_available_moves()
    print(k_pos)