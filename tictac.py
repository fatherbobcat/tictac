# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:49:59 2017

@author: lsha
"""

from random import randint
import time
from copy import deepcopy

class ticTac:
    
    def __init__(self):

        self.board = [[""]*3 for i in range(3)]
        
    def printBoard(self):
        for i in range(3):
            print (self.board[i])
            
    def placeMove(self, location, symbol):
        self.board[location[0]][location[1]] = symbol
    
    def isValidMove(self, location):
        return self.board[location[0]][location[1]] ==""
    
    def gameWon(self):
        rowWin = False
        columnWin = False
        diagonalWin = False
        
        for i in range(3):
            if rowWin or columnWin:
                break
            if self.board[i][0] != "":
                rowWin = self.board[i][0]==self.board[i][1]==self.board[i][2]
            if self.board[0][i] != "":
                columnWin = self.board[0][i]==self.board[1][i]==self.board[2][i]
        
        if self.board[1][1]!= "":
            diagonalWin = (self.board[0][0] ==self.board[1][1] == self.board[2][2]) or (self.board[2][0]==self.board[1][1]==self.board[0][2])
        
        return rowWin or columnWin or diagonalWin
        
    def gameDone(self):
        
        gameWon = self.gameWon()
        gameDone = True
        if not gameWon:
            gameDone = True
            for i in range(3):
                for j in range(3):
                    gameDone = gameDone and self.board[i][j] !=""
                         
        return gameDone or gameWon
    
    def AIMove(self):
        move= (randint(0,2), randint(0,2))
        
        while not self.isValidMove(move):
            move= (randint(0,2), randint(0,2))
        self.placeMove(move,"O")
        time.sleep(1)
        print("AI Moved")
        self.printBoard()
    
    def smartAIMove(self):
        moves = self.getAvailableMoves()
        utility = float("-inf")
        endMove = None
        for x in moves:
            copy = deepcopy(self.board)
            copy[x[0]][x[1]] = "O"
            util = self.getUtility(copy)
            if util>utility:
                utility = util
                endMove = x
        self.placeMove(endMove,"O")
        print("AI Moved")
        self.printBoard()
                
    
    def getAvailableMoves(self):
        moves =[]
        for i in range(3):
            for j in range(3):
                if self.isValidMove((i,j)):
                    moves.append((i,j))
        return moves
    
    def getUtility(self, board):
                
        util = 0
        for x in range(3):
            utilRow = 0
            for y in range(3):
                if board[x][y]=="O":
                    utilRow = utilRow+1
                if board[x][y]=="X":
                    utilRow = utilRow-1
            if utilRow > util:
                util= utilRow
        
        util1 = 0
        for x in range(3):
            utilCol = 0
            for y in range(3):
                if board[y][x]=="O":
                    utilCol = utilCol+1
                if board[y][x]=="X":
                    utilCol = utilCol-1
            if utilCol > util1:
                util1= utilCol
        
        util2 = 0
        util3 = 0
        if board[0][0] =="O":
                util2 = util2+1
        elif board[0][0]=="X":
                util2 = util2-1
        if board[1][1] == "O":
                util2 = util2+1
        elif board[1][1]=="X":
                util2 = util2-1
        if board[2][2] =="O":
                util2 = util2+1
        elif board[2][2]=="X":
                util2 = util2-1
        if board[0][2] =="O":
                util3 = util3+1
        elif board[0][2]=="X":
                util3 = util3-1
        if board[1][1] == "O":
                util3 = util3+1
        elif board[0][2]=="X":
                util3 = util3-1
        if board[2][0] =="O":
                util3 = util3+1
        elif board[0][2]=="X":
                util3 = util3-1
        
        return max(util, util1, util2, util3)

#This will let two players play a game of tic tac toe on a terminal
def main():
    
    game = ticTac()
    print ("You have started a game of Tic Tac Toe. May the odds be ever in your favor.")
    ai = input("Do you want to play with an AI? Y/N ")
    if ai=="Y":
        mode = input("Please enter 1 for Easy Mode, 2 for Medium Mode")
        print("Player starts.")
    else:
        print ("X starts.")
    game.printBoard() 
    
    symbol = "X"
    
    while not game.gameDone():
            
        move = input("Place your move. Format: 'row,col' ")
        move = move.split(',')
        move = list(map(int, move))
        
        move[:] = [x-1 for x in move] 
        while not game.isValidMove(move): 
            move = input("This square has already been claimed! Choose another square. ")
            move = move.split(',')
            move = list(map(int, move))
            move[:] = [x-1 for x in move]
        game.placeMove(move,symbol)
        game.printBoard()
        
        if ai == "N":
            if symbol == "X":
                symbol = "O"
            else:
                symbol="X"
        elif not game.gameDone():
            if mode == "1":
                game.AIMove()
            if mode=="2":
                game.smartAIMove()
                
        else:
            symbol = "O"
            break
    
    if symbol =="X":
        symbol ="O"
    else:
        symbol="X"
    if game.gameWon():
        print ("Hooray! "+symbol+" won the game!")
    else:
        print ("It's a draw. We're all winners here!")
    
            
        
if __name__=='__main__': main()
