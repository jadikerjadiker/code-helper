
#the code below works as expected (returns a new table with the values of a reversed)
a = ["hello", "goodbye", "check", "one", "two"]
b = [1, 3, 5, 6, 8]

k=0
def getKey(item):
    global k
    k+=1
    print("getKey")
    print(item)
    print(k)
    return 10-k
    
sorted(a, key=getKey)
print(a)
print(sorted(a, key=getKey))
del k