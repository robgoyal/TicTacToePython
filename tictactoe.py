# Name: tictactoe.py
# Author: Robin Goyal
# Last-Modified: December 9, 2017
# Purpose: Play a game of tictactoe

from board import Board
from player import Player
import random


class TicTacToe(object):
    def __init__(self):
        self.gameBoard = Board()

        # Initialize an array of Player objects for X and O
        playerX = Player(Player.marks[0], self.gameBoard)
        playerO = Player(Player.marks[1], self.gameBoard)
        self.players = [playerX, playerO]

        # Choose the first player (0 or 1 in players array)
        self.firstTurn = round(random.random())

    def playGame(self):
        '''
        Play a game of Tic Tac Toe after random choosing a player
        '''

        print("This is a game of TicTacToe!")
        print("Randomly choosing a Player!")

        firstPlayer = self.players[self.firstTurn]
        print("The first player is Player {}\n".format(firstPlayer.getMark()))

        turns = 0
        while(self.gameBoard.getWinner() is None) and turns < 9:
            print("Turns: {}".format(turns))
            self.gameBoard.printBoard()
            self.players[(turns + self.firstTurn) % 2].takeTurn()
            turns += 1

        if turns == 9:
            print("No Winner")
        else:
            print("Player {} Won!".format(self.gameBoard.getWinner().getMark()))


if __name__ == "__main__":
    newGame = TicTacToe()
    newGame.playGame()
