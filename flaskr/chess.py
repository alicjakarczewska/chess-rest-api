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


    def list_available_moves():      
      logger.info("Not implemented")


    def validate_move(dest_field):
      logger.info("Not implemented")

    