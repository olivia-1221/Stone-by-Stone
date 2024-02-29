import numpy as np

"""
This class represents the Go board, with methods for placing stones and retrieving the state of intersections.
The board attribute is a two-dimensional array where each element represents an intersection, and the value of the element
indicates the state of that intersection (0 for empty, 1 for black stone, and -1 for white stone).
"""

class GoBoard:
    # Initialize empty board
    def __init__(self, size):
        self.size = size
        self.board = np.zeros((size, size))
    
    # Place stone of specified color at coordinates (x, y)
    def place_stone(self, x, y, color):
        self.board[y][x] = color
        
    # Get the color of the stone at coordinates (x, y)
    # TODO: explanation of coordinates
    def get_stone_at(self, x, y):
        return self.board[y][x]
    
    # Determine if the move is legal
    def is_legal_move(self, x, y, color):
        # TODO: must have at least one liberty or be connected to a group with at least one liberty
        return 0

    # Checks if the most recent move was a capture
    def is_capture(self, x, y, color):
        # TODO: must have captured the stone/group's final liberty
        return 0

    # TODO: keep track of groups somehow (orthogonally connected stones of the same color)
    # TODO: tests
