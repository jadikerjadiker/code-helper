from LazerGame import *
from BruteForceSolver import *
from Challenge import *
from ActualPuzzles import *


#Main

def main():
    puzzle31()
    
   
def testPuzzle55Solution():
    ch = Challenge()
    ch.setTargetAmt(2)
    ch.addToBoard("laserstarter", 7, 2, "mirror", 9, 0, "splitter", 12, 0, "mirror", 13, 2, "checkpoint", 14, 0, "mirror", 17, 0, "mirror", 20, 1, "mirror", 23, 0, "dblmirror", 24, 1)
    game=Game(ch.board, ch.targetAmt)
    game.printBoardState()
    game.stepThroughGame()
        
def funPuzzle1():
    ch = Challenge()
    ch.addToBoard("laserstarter", 1, 1)
    ch.addToPiecesToPlace("dblmirror", "dblmirror", "target")
    ch.setTargetAmt(1)
    bfs = BruteForceSolver()
    print("Solving...")
    sol = bfs.solve(ch)
    print("Finished solving:")
    if sol:
        print("Solution found!")
        printGame = Game(sol)
        printGame.printBoardState()
    else:
        print("Unsolvable!")

def testPuzzle1():
    ch = Challenge()
    ch.addToBoard("laserstarter", 1, "?", "blocker", 4, "?", "checkpoint", 18, "?", "splitter", 19, "?", "target", 24, "?", "target", 20, "?", "dblmirror", 16, "?")
    ch.addToPiecesToPlace()
    ch.setTargetAmt(2)
    bfs = BruteForceSolver()
    print("Solving...")
    sol = bfs.solve(ch)
    print("Finished solving:")
    if sol:
        print("Solution found!")
        printGame = Game(sol)
        printGame.printBoardState()
    else:
        print("Unsolvable!")

def testPuzzle2():
    def allTable():
        return [0, 1, 2, 3]
    def twoTable():
        return [0, 1]
    testGame = Game()
    pD = blank25Table()
    testGame.addPiece("laserstarter", 1, 0)
    pD[1] = allTable()
    testGame.addPiece("blocker", 4, 0)
    pD[4] = [0]
    testGame.addPiece("dblmirror", 16, 0)
    pD[16] = twoTable()
    testGame.addPiece("checkpoint", 18, 0)
    pD[18] = twoTable()
    testGame.addPiece("splitter", 19, 0)
    pD[19] = twoTable()
    testGame.addPiece("target", 20, 0)
    pD[20] = allTable()
    testGame.addPiece("target", 24, 0)
    pD[24] = allTable()

    bfs = BruteForceSolver()
    print("Solving...")
    sol = bfs.testRotations(testGame, pD)
    print("Finished solving:")
    if sol:
        print("Solution found!")
        printGame = Game(sol)
        printGame.printBoardState()
    else:
        print("Unsolvable!")

def testPuzzle3():
    def allTable():
        pass
    def twoTable():
        pass
    testGame = Game()
    pD = blank25Table()
    testGame.addPiece("laserstarter", 1, 2)
    pD[1] = allTable()
    testGame.addPiece("blocker", 4, 0)
    pD[4] = [0]
    testGame.addPiece("dblmirror", 16, 0)
    pD[16] = twoTable()
    testGame.addPiece("checkpoint", 18, 1)
    pD[18] = twoTable()
    testGame.addPiece("splitter", 19, 0)
    pD[19] = twoTable()
    testGame.addPiece("target", 20, 1)
    pD[20] = allTable()
    testGame.addPiece("target", 24, 2)
    pD[24] = allTable()

    testGame.stepThroughGame()
    
        
main()
