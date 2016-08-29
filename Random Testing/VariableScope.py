def test():
    def printA():
        print(a)
    
    a = "hello"
    printA()

def test2():
    def printA():
        def printIt():
            print(a)
        
        printIt()
        
def test3():   
    def printB():
        def printIt():
            print(b)
        
        printIt()
    printB()
    
def test4():
    def printA():
        def somethingElse():
            pass
        print(a)
        ra = a[2]
        a = ra
        
    a = [1, 2, 3]
    while True:
        printA()
        
test4()