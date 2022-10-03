from abc import ABCMeta

class Figure(metaclass=ABCMeta):

    def __init__(self, position=None):
      self._position=position
      

    def list_available_moves():      
      logger.info("Not implemented")


    def validate_move(dest_field):
      logger.info("Not implemented")