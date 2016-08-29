11/31/2015

#test to see if when I read a line with "\n" in it and then print it if it prints a line.

#basically, everything works the way you think it would.
#"\n" is just how you represent the newline character in a string when typing it for a compiler.
#But this also means that for the time being, section symbols can't have new lines in them because the finder doesn't look for them on new lines.
#which in some ways is constrictive, but in other ways makes sense for readability.
with open("TheFile.txt") as f:
    a = f.readline()
    print(a) #does not print a new line!
    b = f.readline()
    print(a.find("\\n"))
    print(a.find("\n"))
    print(b.find("\n"))
    
    