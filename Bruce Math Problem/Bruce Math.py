import itertools as it
b = [5, None, None, 3, None, None, None, None , None]

def addToSlot(thing, slotNum):
    #print("added {} to slot {}".format(thing, slotNum))
    t1 = thing[0]
    t2 = thing[1]
    if slotNum == 0:
        b[1] = t1
        b[2] = t2
    if slotNum == 1:
        b[5] = t1
        b[8] = t2
    if slotNum == 2:
        b[6] = t1
        b[7] = t2

def hasWon():
    num = b[0]+b[3]+b[6]
    if b[0]+b[1]+b[2]==num and b[2]+b[5]+b[8]==num and b[6]+b[7]+b[8]:
        return True

def reverse(thing):
    return [thing[1], thing[0]]

theList = [[2, 4], [3, 6], [2, 5]]
for i in range(3):
    j = i+1
    ans = []
    for i2 in range(j):
        ans.append(1)
    while len(ans)<3:
        ans.append(0)
    for i3, v1 in enumerate(list(it.permutations(ans))):
        for i3, perm in enumerate(v1):
            if perm == 1:
                theList[i3] = reverse(theList[i3])
        print("ans: {}".format(v1))
    
        for i4, v2 in enumerate(list(it.permutations(theList))):
            #print("first element:", v2[0])
            for num, thing in enumerate(v2):
                addToSlot(thing, num)
            if hasWon():
                print("did it!")
                print(v2)
                raise RuntimeError("Success! {}".format(v2))
    
    