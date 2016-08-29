#11/30/2015

print("start")
print("") #this prints a blank line
print('Hi')

with open("TheFile.txt") as fileobj:
    for line in fileobj:  
        for ch in line:
            print(ch)
            '''
            if ch=="\n":
                print "newline"
            else:
                print ch
            '''