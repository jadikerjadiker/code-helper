j = 20
total = 0
for i in range(19):
    if total>2674:
        print(i)
    total+=j
    j = j + 20
    
print(total, i)