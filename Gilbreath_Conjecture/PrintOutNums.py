import numpy as np

###### list creation ######
def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def oddsFrom1to(n):
    ans = []
    for i in range(n):
        if i%2 == 1:
            ans.append(i)
    return ans
    
def oddsbetween(a, b):
    ans = []
    while a<b:
        a+=1
        if a%2==1:
            ans.append(a)
    return ans

def getPrimeList(n): #converts the array to a list
    return primesfrom2to(n).tolist()

###### list creation end ######




###### Gilbreath calculations ######
def computeNextLine(anArray):
    ans = []
    lastIndex = len(anArray)-1
    #print("lastIndex: "+str(lastIndex))
    for index, val in enumerate(anArray):
        #print("index: "+str(index))
        if index<lastIndex:
            ans.append(abs(val-anArray[index+1]))
        else:
            return ans
            
def computeGilbreathPrimeLists(n, printOut = False):
    return computeGilbreathLists(primesfrom2to(n), printOut)
    
def computeGilbreathLists(initArray, printOut = False):
    def printOutAns(finalAns):
        for val in finalAns:
            print(val)
    
    ans = [[]]
    maxIndex = -1 #figure out the max index of array while setting up ans
    for val in initArray: #set up
        ans[0].append(val)
        maxIndex+=1
    for _ in range(maxIndex):
        #print("last ans: {}".format(ans[-1]))
        ans.append(computeNextLine(ans[-1]))
    if printOut:
        printOutAns(ans)
    return ans
 
 
###### Gilbreath calculations end ######


###### testing ######

'''
Josh's idea:
Since all the primes are odd (except for 2) the distance between them will always be an even number.
All the numbers travel down the line...
and the result of the distance operation is always less than the largest number in the operation (|a-b|<=man(a, b)):
as the numbers travel, they always go down to at least 2 by the second number.

Josh's Theorem:
The Gilbreath conjecture will hold for any list of odd numbers
'''

def see100():
    computeGilbreathPrimeLists(100, True)
    
def againstJosh1(): #Gilbreaths
    init = getPrimeList(100)
    init.insert(4, 9)
    computeGilbreathLists(init, True)
    
def againstJosh2(): #Gilbreaths
    init = oddsFrom1to(50)
    init[0] = 2
    computeGilbreathLists(init, True)
    
def againstJosh3(): #Does not Gilbreath! Multiple lines start with 19.
    init = oddsFrom1to(40)
    init.extend(oddsbetween(60, 80))
    init[0] = 2
    computeGilbreathLists(init, True)
    
def run():
    againstJosh3()

###### testing end ######

###### main program ######

run()

###### main program end ######
