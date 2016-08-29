from MyUsefulFunctions import *
from LazerGame import *

#Made in 2015 by London Lowmanstone IV
#Defines the Challenge class which provides a way to hold and easily change information associated with solving a challenge card

class Challenge():
    def __init__(self, setupBoard = blank25Table(), piecesToPlace = [],  targetAmt = 1):
        self.board = setupBoard #the board that holds the pieces (see the board class)
        self.piecesToPlace = piecesToPlace #the non-stationary pieces that need to be placed onto the board
        self.targetAmt = targetAmt #how many targets need to be hit to complete the challenge

    def addBoardPieces(self, *args):
        for piece in args:
            self.addBoardPiece(piece)

    def addBoardPiece(self, p):
        if self.board[p.pos]:
            print("addPiece: cannot put piece {} at {} because there is already a {} there.".format(p.type, p.pos, self.board[p.pos].type))
        else:
            self.board[p.pos]=p

    def addPiecesToPlace(self, *args):
        for piece in args:
            #print("Add pieces to place added piece {}.".format(piece))
            self.addPieceToPlace(piece)

    def addPieceToPlace(self, p):
        self.piecesToPlace.append(p)

    def setTargetAmt(self, num):
        self.targetAmt = num

    def addToBoard(self, *args):
        for s in range(0, maxn(args), 3):
            #print("Challenge add to board added {} at {} with rotation {}.".format(args[s], args[s+1], args[s+2]))
            self.addBoardPiece(Piece(args[s], args[s+1], args[s+2]))

    def addToPiecesToPlace(self, *args):
        for name in args:
            self.addPieceToPlace(Piece(name))
