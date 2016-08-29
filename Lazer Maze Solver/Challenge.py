from MyUsefulFunctions import *
from LazerGame import *

class Challenge():
    def __init__(self, setupBoard = blank25Table(), piecesToPlace = [],  targetAmt = 1):
        self.board = setupBoard
        self.piecesToPlace = piecesToPlace
        self.targetAmt = targetAmt

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
