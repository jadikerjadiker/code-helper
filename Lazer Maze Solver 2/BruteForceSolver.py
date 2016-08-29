from MyUsefulFunctions import *
from DirectionFunctions import *
from LazerGame import *
from Challenge import *
import copy

#Made in 2015 by London Lowmanstone IV
#This is the program that actually solves the laser maze
#It tries every single possibility until it finds a winning setup and then returns the board

'''
25 Tables:
BFS.possDirs

Lists:
BFS.openSpaces
'''

'''
I'm going to make notes here as I try to remember what things stand for and how this works.
pTP is short for "Pieces to Place". I'm pretty sure this contains a list of the pieces not inherently set up on the board.
'''

#todo del print stuff
def log(*stuff):
    print(stuff)


class BruteForceSolver():
    
    def __init__(self):
        pass

    def solve(self, challenge):
        placePieces = copy.deepcopy(challenge.piecesToPlace)
##        log("Pieces to place: {}.".format(placePieces))
        board = copy.deepcopy(challenge.board)
        targetAmt = challenge.targetAmt
        testGame = Game(board, targetAmt)
        pD, oS = self.setFirstPositionSetup(board, placePieces) #nts: poss prob this may cause issues with unpacking only one None when it fails
        #log("FirstPositionSetup finished")
        #dp
        log("Here is the first position, followed by the possible directions and open Spaces")
        testGame.printBoardState()
        #print25Table(pD)
        #log(oS)
##        log("FirstPositionSetup printout finished")
        rTestGame = self.testRotations(testGame, pD) #a game that has all possible rotations of the pieces tested on it
##        log("rTestGame done testing rotations! Here's the possible directions afterwards:")
##        print25Table(pD)
        if rTestGame:
            return rTestGame
##        log("NOW SETTING NEXT POSITION!")
        nxtPos = self.setNextPosition(testGame.board, placePieces, pD, oS)
  			
        while nxtPos:
            rTestGame = self.testRotations(testGame, pD)
            if rTestGame:
                break
            nxtPos = self.setNextPosition(testGame.board, placePieces, pD, oS)
            #log("After new setup:")
            #testGame.printBoardState()
            #testGame.stepThroughGame()
        if nxtPos:
            return rTestGame
        else:
            return False

    def setFirstPositionSetup(self, board, pTP):
        openSpaces = [] #list of all the empty spaces in the board after the setup
        possDirs = blank25Table()
        for i in range(1, 26):
            piece = board[i]
            #log(piece)
            if piece: #if there's a piece in this slot
                if piece.direction=="?":
                    possDirs[i] = self.calcPDForPieceType(piece.type)
                    piece.direction = 0 #assuming that all unknown pieces can start in direction 0
                else:
                    possDirs[i]=[piece.direction] #the only direction this piece can go in is the one it was given
            else:
                openSpaces.append(i)
        #log(openSpaces)
        #log(pTP)
        if maxn(openSpaces)<maxn(pTP):
            print("setFirstPositionSetup: not enough spaces for the pieces to fit!")
            return None

        for index, piece in enumerate(pTP):
            slot = openSpaces[0]
            piece.pos = slot
            piece.direction = 0
            board[slot] = piece
            possDirs[slot] = self.calcPDForPieceType(piece.type)
            openSpaces.pop(0)
        return possDirs, openSpaces

    def setNextPosition(self, board, pTP, pD, oS):
        pTPMax = maxn(pTP)
        #log("Here's pTP and maxn(pTP)")
        #log(pTP)
##        log(pTPMax)
##        log("Here's the openSpaces I recieved: {}.".format(oS))
        for i in range(0, pTPMax+1): #iterate backwards through pTP (pieces to place)
            revI = pTPMax-i
            piece = pTP[revI]
            pPos = piece.pos
            op = self.getOpenSlot(pPos, oS) #shortened open to op
##            log("revI: {}.".format(revI))
            if op: #if there is an open slot
                #COMMENTER!
                blockout = 0
                if i+1>blockout:
                    print("Move of magnitude {}.".format(i+1)) #i+1 so that the magnitude starts at 1 (so it's more human)
                self.movePiece(piece, op, board, pD, oS) #move the piece to the open slot
                #log("moved piece {}".format(piece.type))
                for j in range(revI+1, pTPMax+1): #setup all the pieces that were taken off the board since they had nowhere to go
                    piece=pTP[j]
                    newSlot = self.getOpenSlot(0, oS)
                    self.setupMovedPiece(piece, newSlot, board, pD, oS)
                return True
            else:
                if revI==0: #if there are no more pieces to try to move, return False (no solutions found)
##                    log("Here's the piece's position and openSpaces")
##                    log(pPos)
##                    log(oS)
##                    log("couldn't find a next position!")
                    return False
                self.takedownMovedPiece(piece, board, pD, oS) #take that piece off the board and get it ready to be placed back down.
##        log("Set next position failed!")
        return None
    
    #t is an array of open slot numbers
    #returns a slot number greater than @param laterThan.
    #if there is none in the array, it returns None
    def getOpenSlot(self, laterThan, t):
        for op in t:
            if op>laterThan:
                return op
        return None



    def addOpenSlot(self, num, t): #nts: poss prob this may cause issues...
##        log("addOpenSlot begins, here's the number and oS (called t here).")
##        log(num)
##        log(t)
        for index, low in enumerate(t):
            if low>num:
                where=index
                break
        try:
            where
        except:
            where = maxn(t)+1
        t.insert(where, num)
##        log("Here's t after the insert")
##        log(t)

    def deleteOpenSlot(self, num, t):
        for i, check in enumerate(t):
            if check==num:
                t.pop(i)
                return

    def movePiece(self, piece, newPos, board, pD, oS):
##        log("Moving piece {} from pos {} to pos {}.".format(piece.type, piece.pos, newPos))
        self.takedownMovedPiece(piece, board, pD, oS)
        self.setupMovedPiece(piece, newPos, board, pD, oS)
    
    #remove all the references of the piece from the board and and the rotations
    def takedownMovedPiece(self, piece, board, pD, oS): #nts: poss prob I think the issue has to do with this
##        log("taking down {} at {}, here's openSlots:".format(piece.type, piece.pos))
##        log(oS)
        curPos = piece.pos #save where I'm taking it off from
        board[curPos] = None #take it off the board
        piece.tempRotations = pD[curPos] #save rotations
        pD[curPos] = None #delete its rotations from the possibleDirections (pD) array
        self.addOpenSlot(curPos, oS) #tell it that its new spot is open
    
    #set up a piece in a new spot, resetting its rotation.
    def setupMovedPiece(self, piece, newPos, board, pD, oS):
        piece.pos = newPos
        board[newPos] = piece
        pD[newPos] = piece.tempRotations
        piece.tempRotations = None
        self.deleteOpenSlot(newPos, oS)

    #gives back a table with all the different ways this piece can be rotated.
    #short for calculatePossibleDirectionsForPieceType
    def calcPDForPieceType(self, t):
        if t=="blocker":
            return [0]
        elif t=="dblmirror" or t=="splitter" or t=="checkpoint":
            return [0, 1]
        else:
            return [0, 1, 2, 3]

    
    #returns a list with the open spaces in the board
    def getOpenSpaces(self, b):
        ans = []
        for i in range(1, 26):
            piece = b[i]
            if not piece:
                ans.append(i)
        return ans

    #tests all the rotations of a given board setup
    #setupGame is a setup game with the board of all the pieces on it.
    #possDirections is a 25table where the possDirections[i] corresponds to the directions that the piece at setupGame.board[i] can be rotated.
    #returns the solution board if there is one, returns False otherwise.
    def testRotations(self, setupGame, possDirections):
        #dp
        debug = 0
        d = copy.deepcopy(possDirections)
        g = Game(setupGame.board, setupGame.targetAmt)
        b = g.board #any change to b will actually change the board of g since the board is a table
        
        #dp
        tester = Game(setupGame.board)
        tester.printBoardState()
        
        ans = False
        self.setFirstRotationSetup(b, d)
        if not b:
            return False
        else:
            #log("THIS IS RIGHT AFTER THE ROTATION SETUP!")
            #g.printBoardState()
            #g.stepThroughGame()
            #log("step through done")
            #log(g.getEndResult())
            #g.stepThroughGame()
            if g.getEndResult():
                #log("Found answer!")
                return b
        nxtR = self.setNextRotation(b, d)
        while nxtR:
            #dp
            '''
            if if b[3] and b[3].type=="laserstarter" and b[3] and b[3].type=="mirror" and debug<100:
                #log("rotation game")
                #g.printBoardState()
                g.stepThroughGame()
                debug+=1
            '''
                
            if g.getEndResult():
                break
            nxtR = self.setNextRotation(b, d)
##            log("testRotations: BOARD STATE")
##            g.printBoardState()
        if nxtR:
            return b
        else:
            return False

    def setFirstRotationSetup(self, board, possDirections):
        #log("setFirstRotationSetup start")
##        smallgame = Game(board)
##        log("board gotten")
##        smallgame.printBoardState()
##        log("done")
        #log("rotation table gotten")
        #print25Table(possDirections)
##        log("done")
        for i in range(1, 26):
            r = possDirections[i]
            if r:
                #log(r)
                #log(i)
                #log(maxn(board), maxn(r))
                board[i].direction = r[0]
        #log("first rotation")
        #Game(board).printBoardState()
##        log("done")
##        log("first rotation table")
##        print25Table(possDirections)
        #log("First Rotation Setup done")
        

    #sets b to the next rotation for the board. Returns false if there is no more rotations
    #d is the array of directions that the pieces can move
    def setNextRotation(self, b, d):
        #log("Directions:")
        #print25Table(d)
        toChange = []
        changeNum = 0
        while True:
            changeP = None
            changePNum = self.getRotationNumFromEnd(d, changeNum) #changeP is short for changePieceNumber #gets the possDirections for the changeNum to last piece (second to last piece if changeNum is 2)
            #log("Here's changePNum: "+str(changePNum))
            if changePNum:
                #log("Here's changePNum inside: "+str(changePNum))
                #log(b)
                changeP = b[changePNum] #assumes that the number actually does give a piece
            else: #all the pieces have hit their max; I can't set a new rotation
                return False
            myDs = d[changePNum] #short for myDirections
##            log("current direction and then myDs")
##            log(changeP.direction)
##            log(myDs)
            curRKey = getElementFirstKey(changeP.direction, myDs)
##            log("curRKey gotten: {}".format(curRKey))
##            log("maxn(myDs): {}".format(maxn(myDs)))
##            log("Here's myDs: ")
##            log(myDs)
            if curRKey==maxn(myDs): #if I'm at the last rotation I can be at before resetting the one above me
                toChange.append(changeP) #I should be reset once something higher than me can change
                changeNum+=1
            else:
                changeP.direction = myDs[curRKey+1]
                for otherP in toChange:
                    otherP.direction = d[otherP.pos][0]
                return True

    #gets the possDirections for the changeNum to last piece (second to last piece if changeNum is 2)
    def getRotationNumFromEnd(self, rotations, targetNum):
        num = 0
        for i in range(1, 26):
            r = rotations[26-i]
            if r:
                if num==targetNum:
                    return 26-i
                else:
                    num+=1
        return None #targetNum is too high; there is no such piece
                
        
            




            
                    
            










                    
