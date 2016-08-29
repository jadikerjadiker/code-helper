import TimeToRun as ttr

a = []
b = []
for i in range(1000):
    a.append((1, 2, 3))
for i in range(1000):
    b.append(1)
    b.append(2)
    b.append(3)

def goThroughA():    
for i, val in enumerate(a):
    