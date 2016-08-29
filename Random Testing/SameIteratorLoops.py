#so you can use the same variable inside a different function and things will work out fine.
#but if you use it nested, the value of i is determined by where it was used last (the for loop is considered to be using it)

'''
def loopThis(num):
    for i in range(num):
        print("loopThis: {}".format(i))
        
for i in range(5):
    print(i)
    loopThis(2)
'''

for i in range(3):
    print("outer first: "+str(i)) #here, i refers to the outer for loop
    for i in range (4):
        print("inner: "+str(i)) #here, i refers to the inner for loop
    print("outer second: "+str(i)) #here, i STILL refers to the inner for loop!
print("final: "+str(i)) #here, i STILL refers to the inner for loop!
    