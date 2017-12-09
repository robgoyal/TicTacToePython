# Name: board.py
# Author: Robin Goyal
# Last-Modified: December 9, 2017
# Purpose: Implement the Board class for the game

from player import Player


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
        left_col = (grid[0][0] == piece) and (grid[1][0] == piece) and (grid[2][0] == piece)
        mid_col = (grid[0][1] == piece) and (grid[1][1] == piece) and (grid[2][1] == piece)
        right_col = (grid[2][0] == piece) and (grid[2][1] == piece) and (grid[2][2] == piece)
        left_diag = (grid[0][0] == piece) and (grid[1][1] == piece) and (grid[2][2] == piece)
        right_diag = (grid[2][0] == piece) and (grid[1][1] == piece) and (grid[0][2] == piece)

        return any([top_row, mid_row, bot_row, left_col, mid_col, right_col, left_diag, right_diag])

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
        if self.checkWinner(player):
            self.setWinner(player)


def main():
    board = Board()
    board.printBoard()

    players = [Player("X", board), Player("O", board)]
    turns = 0

    while (board.getWinner() is None) and turns < 9:
        print("Turns: {}".format(turns))
        print(board.board)
        print(board.winner)
        board.printBoard()
        players[turns % 2] .takeTurn()
        turns += 1

    if turns == 9:
        print("No Winner!")
    else:
        print("Player {} Won!".format(board.getWinner().getMark()))


if __name__ == "__main__":
    main()
