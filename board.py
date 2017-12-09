# Name: board.py
# Author: Robin Goyal
# Last-Modified: December 9, 2017
# Purpose: Implement the Board class for the game


class Board(object):

    def __init__(self):

        # Initialize 3x3 board of None's
        self.board = [[None] * 3 for x in range(3)]
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

    def checkWinner(self, player, x, y):
        '''
        x -> int: row of board
        y -> int: col of board
        return -> bool

        Check if the player that made a move has won
        '''

        grid = self.board

        # Optimized solution retrieved from
        # https://codereview.stackexchange.com/questions/24764/tic-tac-toe-victory-check

        # Don't need to check rows and columns where the move wasn't made
        # Adapted solution to check that the values aren't equal to None
        rows = grid[x][0] == grid[x][1] == grid[x][2] == player.getMark()
        cols = grid[0][y] == grid[1][y] == grid[2][y] == player.getMark()
        prim_diag = grid[0][0] == grid[1][1] == grid[2][2] == player.getMark()
        sec_diag = grid[0][2] == grid[1][1] == grid[2][0] == player.getMark()

        return any([rows, cols, prim_diag, sec_diag])

    def isLocationValid(self, x, y):
        '''
        x -> int: row of board
        y -> int: col of board
        return -> bool: indicating that the position is valid
        '''
        return (0 <= x <= 2) and (0 <= y <= 2)

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
        print()

    def placeMark(self, player, x, y):
        '''
        player -> Player: player who's placing piece
        x -> int: row of grid to place mark on
        y -> int: col of grid to place mark on

        Place mark (X or O) and check if player won after move
        '''

        self.board[x][y] = player.getMark()

        # Set the status of the winner if winner placed a game winning piece
        if self.checkWinner(player, x, y):
            self.setWinner(player)
