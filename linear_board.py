from list_utils import find_streak
from settings import BOARD_LENGTH, VICTORIY_STRIKE

class LinearBoard():
    """
    Clase que representa un tablero de una sola columna.
    x es un jugador
    o otro jugador
    None es un espacio vacío
    """

    def __init__(self):
        """
        Una lista de None.
        """

        self._column = [None for i in range(BOARD_LENGTH)]

    def add(self, char):
    
        """
        Juega en la primera posición disponible
        """
        # Siempre y cuando no esté lleno...
        if not self.is_full():
            # buscamos la primera posición libre
            i = self._column.index(None)
            # y lo sustituimos por char
            self._column[i] = char

    def is_full(self):
        """
        Determina cuando está lleno el tablero.
        """
        return self._column[-1] != None

    def is_victory(self, char):
        return find_streak(self._column, char, VICTORIY_STRIKE)

    def is_tie(self, char1, char2):
        """
        No hay victoria ni de char1 ni de char2
        """
        return (self.is_victory('x') == False and self.is_victory('o') == False)