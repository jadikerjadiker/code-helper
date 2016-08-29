#enumerate starts at the cursor of the file! Be careful! Make sure you start at the start of a file if that's where you want to be!
#11/29/15
'''
Test to see if enumerating a file always starts from the start, or if it starts as the cursor.
'''

with open("TheFile.txt") as f:
    print(f.readline())
    print(f.readline())
    for lineNum, line in enumerate(f):
        print("lineNum: {}".format(lineNum))
        print("line: {}".format(line))