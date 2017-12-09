# Name: board.py
# Author: Robin Goyal
# Last-Modified: December 9, 2017
# Purpose: Implement the Board class for the game


class Board(object):

    def __init__(self):

        # Initialize 3x3 board of None's
        self.board = [[None] * 3] * 3
        self.winner = None

    def getWinner(self):
        '''
        return -> Player

        return the player mark if a player has won
        '''

        return self.winner

    def setWinner(self, player):
        '''
        player -> Player
        Set the winner to the player
        '''

        self.winner = player

    def checkWinner(self, player):
        '''
        player -> Player
        return -> bool

        Check if the player that made a move has won
        '''

        grid = self.board
        piece = player.getMark()

        top_row = (grid[0][0] == piece) and (grid[0][1] == piece) and (grid[0][2] == piece)
        mid_row = (grid[1][0] == piece) and (grid[1][1] == piece) and (grid[1][2] == piece)
        bot_row = (grid[2][0] == piece) and (grid[2][1] == piece) and (grid[2][2] == piece)
        # left_col = set([grid[0][0], grid[1][0], grid[2][0]]) == 1
        # mid_col = set(grid[0][1], grid[0][1], grid[0][1]) == 1
        # right_col = set(grid[0][2], grid[1][2], grid[2][2]) == 1
        # left_diag = set(grid[0][0], grid[1][1], grid[2][2]) == 1
        # right_diag = set(grid[0][2], grid[1][1], grid[2][0]) == 1

        return any([top_row, mid_row, bot_row])

    def isLocationEmpty(self, x, y):
        '''
        x -> int: row of board
        y -> int: col of board
        return -> bool: indicating if that position is empty
        '''

        return self.board[x][y] is None

    def printBoard(self):
        '''
        Pretty print the board
        '''

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] is None:
                    print("   ", end="")
                else:
                    print(" {} ".format(self.board[row][col]), end="")
                if col < 2:
                    print("|", end="")
            print()
            if row < 2:
                print("---|---|---")

    def placeMark(self, player, x, y):
        '''
        player -> Player: player who's placing piece
        x -> int: row of grid to place mark on
        y -> int: col of grid to place mark on

        Place mark (X or O) and check if player won after move
        '''

        self.board[x, y] = player.getMark()

        # Set the status of the winner if winner placed a game winning piece
        if self.checkWinner(player):
            self.seetWinner(player)


board = Board()
board.printBoard()
