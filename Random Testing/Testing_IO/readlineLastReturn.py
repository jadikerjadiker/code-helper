with open("TheFile.txt") as f:
    for i in range(10):
        read = f.readline()
        if read == "":
            print("that was empty") #this signifies the end of a file
        if read == None: #this should never be returned
            print("that was none")
        print("Type: {}".format(type(read)))
        print(read)