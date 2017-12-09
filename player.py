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

        x, y = map(int, input("Player {}'s turn. Choose location of mark: ".format(self.mark)).strip().split())

        while not(self.board.isLocationEmpty(x, y)):
            x, y = map(int, input("That location isn't empty! Choose another: ".format(self.mark)).strip.split())

        self.board.placeMark(self, x, y)
