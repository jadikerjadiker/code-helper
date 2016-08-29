#it works, and cloud9 displays it correctly

with open("TheFile.txt", "r+") as file:
    file.readline()
    file.write("Testing1234")