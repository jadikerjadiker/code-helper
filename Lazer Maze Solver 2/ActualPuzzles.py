from LazerGame import *
from BruteForceSolver import *
from Challenge import *

#Actual Puzzles

'''
def template():
    ch = Challenge()
    ch.addToBoard()
    ch.addToPiecesToPlace()
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
'''

def test1():
    ch = Challenge()
    ch.addToBoard("target", 1, 3)
    ch.addToPiecesToPlace("laserstarter", "checkpoint")
    ch.setTargetAmt(1)
    bfs = BruteForceSolver()
    print("Solving...")
    sol = bfs.solve(ch)
    print("Finished solving:")
    if sol:
        print("Solution found!")
        printGame = Game(sol)
        printGame.printBoardState()
        return Game(sol)
    else:
        print("Unsolvable!")
    

def puzzle1():
    ch = Challenge()
    ch.addToBoard("laserstarter", 7, 2, "target", 19, 1)
    ch.addToPiecesToPlace("dblmirror")
    ch.setTargetAmt(1)
    bfs = BruteForceSolver()
    print("Solving puzzle1...")
    sol = bfs.solve(ch)
    print("Finished solving:")
    if sol:
        print("Solution found!")
        printGame = Game(sol)
        printGame.printBoardState()
    else:
        print("Unsolvable!")

def puzzle25():
    ch = Challenge()
    ch.addToBoard("laserstarter", 1, "?", "blocker", 4, 0, "checkpoint", 18, "?", "splitter", 19, "?", "target", 24, "?")
    ch.addToPiecesToPlace("target", "dblmirror")
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
        
def puzzle29():
    ch = Challenge()
    ch.addToBoard("target", 9, 0, "laserstarter", 11, "?", "dblmirror", 14, 0, "target", 24, "?")
    ch.addToPiecesToPlace("mirror", "mirror", "splitter")
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
        
def puzzle30():
    ch = Challenge()
    ch.addToBoard("mirror", 3, "?", "mirror", 7, "?", "mirror", 9, "?", "checkpoint", 12, "?", "target", 17, "?", "splitter", 18, 1, "mirror", 19, "?")
    ch.addToPiecesToPlace("laserstarter")
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

def puzzle31():
    ch = Challenge()
    ch.addToBoard("mirror", 1, "?", "mirror", 4, "?", "checkpoint", 11, 0, "laserstarter", 20, "?", "blocker", 21, 0, "target", 24, "?")
    ch.addToPiecesToPlace("mirror", "dblmirror")
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

def puzzle55():
    ch = Challenge()
    ch.addToBoard("laserstarter", 7, "?", "mirror", 9, "?", "mirror", 13, "?", "mirror", 17, "?", "mirror", 20, "?", "mirror", 23, "?", "dblmirror", 24, "?")
    ch.addToPiecesToPlace("splitter", "checkpoint")
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
        
def puzzle56():
    ch = Challenge()
    ch.addToBoard("target", 2, "?", "laserstarter", 10, "?", "checkpoint", 12, "?", "target", 18, "?", "target", 23, 2)
    ch.addToPiecesToPlace("mirror", "mirror", "splitter", "splitter")
    ch.setTargetAmt(3)
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
        
        
def puzzle58():
    ch = Challenge()
    ch.addToBoard("checkpoint", 8, "?", "mirror", 11, 0, "mirror", 16, "?", "laserstarter", 18, "?", "mirror", 21, 0, "dblmirror", 25, 1)
    ch.addToPiecesToPlace("mirror", "mirror", "splitter")
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
        
def puzzle59():
    ch = Challenge()
    ch.addToBoard("mirror", 6, "?", "blocker", 8, "?", "splitter", 9, "?", "target", 11, "?", "dblmirror", 13, "?", "laserstarter", 17, 0, "checkpoint", 19, "?")
    ch.addToPiecesToPlace("mirror", "mirror", "mirror", "splitter")
    ch.setTargetAmt(3)
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
        
def puzzle60():
    ch = Challenge()
    ch.addToBoard("target", 4, 1, "mirror", 6, 0, "blocker", 12, 0, "checkpoint", 13, "?", "target", 20, 2, "dblmirror", 22, "?")
    ch.addToPiecesToPlace("laserstarter", "mirror", "mirror", "splitter", "splitter")
    ch.setTargetAmt(3)
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
  