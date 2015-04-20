#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK11 synthesizing tasks."""


import time

BOARD = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
         '1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7
}

class ChessPiece(object):
    """A generic chess piece that will provide reusable
    code and storage for our various types of chess pieces.
    """

    prefix = ''

    def __init__(self, position):
        """Checks if starting position is legal."""
        
        if not ChessPiece.is_legal_move(self, position):
            excep = '`{}` is not a legal start position'
            raise ValueError(excep.format(position))
        else:
            self.position = position
            self.moves = []

    def algebraic_to_numeric(self, tile):
        """Converts position on board to algebraic-numeric coordinates."""
        
        if tile[0] in BOARD and tile[1:] in BOARD:
            x_coord = BOARD.get(tile[0])
            y_coord = BOARD.get(tile[1])
            numeric_coord = x_coord, y_coord
            return numeric_coord
        else:
            return None

    def is_legal_move(self, position):
        """Checks if move is legal."""
        
        if not self.algebraic_to_numeric(position):
            return False
        else:
            return True

    def move(self, position):
        """The actual move of the chess piece."""
        
        newposition = self.is_legal_move(position)
        if newposition:
            movehist = (self.prefix+self.position, self.prefix+position,
                               time.time())
            self.moves.append(movehist)
            self.position = position
            return movehist
        else:
            return False
