from DirectionFunctions import *
from MyUsefulFunctions import *

#Made in 2015 by London Lowmanstone IV

'''
This contains the model of the Thinkfun Lazer Maze game.
Splitters create two new laser objects.
It keeps track of repeated positions, so it will never get stuck in an infinite loop.
'''

#Laser Maze Solver

'''
25 Tables:
Game.board
Game.hitPieces

Lists:
Game.lasers
Game.laserStarts
'''

class Game:
    def __init__(self, board = blank25Table(), targetAmt = 0):
        self.board = board
        self.targetAmt = targetAmt
        self.lasers = []
        self.laserStarts = []
        self.hitPieces = blank25Table()

    def start(self):
        for i in range(1, 26):
            piece=self.board[i]
            if piece and piece.type=="laserstarter":
                self.makeLaser(piece.pos, piece.direction)
                return True
        print("Game Start: No laserstarter found!")
        return False

    def step(self):
        self.moveLasers()
        self.doCollisions()

    def moveLasers(self):
        for laser in self.lasers:
            laser.move()

    def doCollisions(self):
        for laser in self.getMovingLasers():
            piece = self.board[laser.pos]
            if piece:
                self.hitPieces[laser.pos]=True
                laser.hitBy(piece)
            
    def getMovingLasers(self):
        ans = []
        for laser in self.lasers:
            if laser.state=="moving":
                ans.append(laser)
        return ans

    def makeLaser(self, pos, direction):
        newLaser = Laser(self, pos, direction)
        rep = False
        #print(self.laserStarts)
        for created in self.laserStarts:
            if created[0]==pos and created[1]==direction:
                rep=True
        if rep:
            newLaser.state="repeat"
        else:
            self.laserStarts.append([pos, direction])
        self.lasers.append(newLaser)
        return newLaser

    def clear(self):
        self.board = blank25Table()
        self.lasers = []
        self.laserStarts = []
        self.hitPieces = blank25Table()

    def addPiece(self, what, where, orientation):
        if self.board[where]:
            print("addPiece: cannot put {} at {} because there is already a {} there.".format(what, where, self.board[where].type))
        else:
            self.board[where]=Piece(what, where, orientation)

    def removePiece(self, where):
        self.board[where] = None

    def isGameAllDone(self):
        #log("getMovingLasers: {}".format(self.getMovingLasers()))
        if maxn(self.getMovingLasers())>-1: #could use len() here, but decided to keep things consistent
            return False
        else:
            return True

    def solutionFound(self):
        def allPiecesHit():
            for i in range(1, 26):
                piece = self.board[i]
                if piece:
                    pieceType = piece.type
                else:
                    pieceType = None
                if pieceType and pieceType!="blocker" and pieceType!="laserstarter" and not(self.hitPieces[i]):
                    return False
            return True

        if not allPiecesHit():
            return False

        hitAmt = 0
        targets = self.getTargets()
        for laser in self.lasers:
            if laser.state=="target":
                for i, target in enumerate(targets): #nts: had to do some porting here; may not work correctly
                    if target:
                        if laser.pos==target.pos:
                            targets[i] = None
                            break
                hitAmt+=1 #nts: poss prob: this can fail since hitting the same target twice would still put the count up to two. But in our situation, that would require two lasers in the same spot, which is counted as a replica, so we're good.

        if maxn(targets)==-1 and hitAmt>=self.targetAmt:
            return True
        else:
            return False

    def getTargets(self):
        ans = []
        for i in range(1, 26):
            piece = self.board[i]
            if piece:
                if piece.type=="target":
                    ans.append(piece)
        return ans

    def clearLasers(self):
        self.lasers = []
        self.laserStarts = []
        self.hitPieces = blank25Table()

    
    def getEndResult(self):
        if self.start():
            i=0
            while not self.isGameAllDone():
                i+=1
                self.step()
                if i>50:
                    print("Taking too long to end the game! Here's the board:")
                    self.printBoardState()
                    raise RuntimeError("Can't find end of game!")
            solFound = self.solutionFound()
            #log("GET END RESULT: {}".format(solFound))
            self.clearLasers() #clears the lasers for the next game
            if solFound:
                return True
            else:
                return False 
        else:
          return None
          
    def printLaserStates(self):
        for num, laser in enumerate(self.lasers):
            print("Laser {}: {} at {} with direction {}".format(num+1, laser.state, laser.pos, laser.direction))

    def printBoardState(self):
        for i in range(1, 26):
            piece = self.board[i]
            if piece:
                print("{} at {} with direction {}".format(piece.type, piece.pos, piece.direction))

    def stepThroughGame(self, clearLasers = True):
        if self.start():
            self.printLaserStates()
            while not self.isGameAllDone():
                self.step()
                self.printLaserStates()
            if self.solutionFound():
                print("Solution found!")
            else:
                print("Solution not found")
        else:
            print("Game not even started!")
        if clearLasers:
            self.clearLasers()

class Laser:
    def __init__(self, game, startSpot, direction):
        self.game = game
        self.pos = startSpot
        self.direction = direction
        self.state = "moving"

    def move(self):
        def lost():
            self.state = "lost"
        if self.state!="moving":
            return
        d = self.direction
        if d==0: #up
            if self.pos<=5:
                lost()
            else:
                self.pos-=5
        elif d==1: #right
            if self.pos%5==0:
                lost()
            else:
                self.pos+=1
        elif d==2: #down
            if self.pos>=20:
                lost()
            else:
                self.pos+=5
        elif d==3: #left
            if self.pos%5==1:
                lost()
            else:
                self.pos-=1
        else:
            print("laser move: unrecognized direction! {}".format(d))

    def hitBy(self, obj):
        def stopped():
            self.state="stopped"
            
        def target():
            self.state = "target"

        def mirror(direction = obj.direction):
            myDir = self.direction
            if direction:
                mirDir = direction
            else:
                mirDir = obj.direction
            if myDir==mirDir: # hit the target
                target()
            elif myDir==dirOpp(mirDir): #coming in from the direction of the mirror, turn direction counterclockwise.
                self.direction = dirCc(self.direction)
            elif myDir==dirOpp(dirC(mirDir)):
                self.direction=dirC(self.direction) #hit mirror other side
            else: #blocked by mirror
                stopped()
                
        def dblmirror():
            myDir = self.direction
            objDir = obj.direction
            if objDir==0 or objDir==2:
                if self.direction==0 or self.direction==1:
                    mirror(2)
                else:
                    mirror(0)
            else:
                if self.direction==1 or self.direction==2:
                    mirror(3)
                else:
                    mirror(1)
        
        def splitter():
            testLaser = Laser(None, self.pos, self.direction)
            testLaser.hitBy(Piece("dblmirror", obj.pos, obj.direction))
            laser1 = self.game.makeLaser(self.pos, self.direction)
            laser2 = self.game.makeLaser(testLaser.pos, testLaser.direction)
            self.state = "split"
            
        def checkpoint():
            myDir = self.direction
            objDir = obj.direction
            if not(myDir==objDir or myDir==dirOpp(objDir)):
                stopped()
        
        t = obj.type
        if t=="laserstarter":
            stopped()
        elif t=="mirror" or t=="target":
            mirror()
        elif t=="dblmirror":
            dblmirror()
        elif t=="splitter":
            splitter()
        elif t=="checkpoint":
            checkpoint()
        elif t=="blocker":
            pass #blockers don't affect lasers
        else:
            print("Laser hit by: object {} not recognized!".format(t))

class Piece():
    def __init__(self, myType, pos = "?", direction = "?"):
        self.type = myType
        self.pos = pos
        self.direction = direction
                
            
                    
                    
                   
        
        


                



