i = 0
test = "test"
while i<len(test):
    print(i)
    if i<3:
        test = test+"hello"
    i+=1
    
# i prints up to 18, so yes, it re-evaluates len(test) every time it goes through the loop.