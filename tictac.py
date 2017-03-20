# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:49:59 2017

@author: lsha
"""

class ticTac:
    
    def __init__(self):

        self.board = [[""]*3 for i in range(3)]
        
    def printBoard(self):
        for i in range(3):
            print self.board[i]
            
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
        

#This will let two players play a game of tic tac toe on a terminal
def main():
    
    game = ticTac()
    print "You have started a game of Tic Tac Toe. May the odds be ever in your favor."
    print "X starts."
    game.printBoard() 
    
    symbol = "O"
    
    while not game.gameDone():
        
        if symbol == "X":
            symbol = "O"
        else:
            symbol="X"
            
        move = input("Place your move. Format: 'row,col' ")
        move = map(int, move)
        move[:] = [x-1 for x in move] 
        while not game.isValidMove(move): 
            move = input("This square has already been claimed! Choose another square. ")
            move = map(int, move)
            move[:] = [x-1 for x in move]
        game.placeMove(move,symbol)
        game.printBoard()
        
        
    if game.gameWon():
        print "Hooray! "+symbol+" won the game!"
    else:
        print "It's a draw. We're all winners here!"
    
            
        
if __name__=='__main__': main()
