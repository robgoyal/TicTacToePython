# Name: player.py
# Author: Robin Goyal
# Last-Modified: Decemeber 9, 2017
# Purpose: Implement the player class for game


class Player(object):

    marks = ["X", "O"]

    def __init__(self, mark, board):
        self.mark = mark
        self.board = board

    def getMark(self):
        '''
        return -> string: mark of the player (X or O)
        '''

        return self.mark

    def takeTurn(self):
        '''
        Places a mark on the board for the player who's turn it is.
        Only applies the mark is the position is empty.
        '''

        try:
            prompt = "Player {}'s turn. Choose row and column for your turn: "
            x, y = map(int, input(prompt.format(self.mark)).strip().split())

        except ValueError:
            # Initialize x and y to -1 to enter while loop
            x, y = -1, -1

        # If the location isn't valid, the while loop condition will short circuit
        while not(self.board.isLocationValid(x, y) and self.board.isLocationEmpty(x, y)):
            prompt = "\tThat location isn't valid! Choose another row and column for your turn: "

            try:
                x, y = map(int, input(prompt.format(self.mark)).strip().split())

            # Except error where user provided a single value. Continue to next iteration of loop
            except ValueError:
                continue

        print()
        self.board.placeMark(self, x, y)
