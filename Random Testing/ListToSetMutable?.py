#The list does not change when values are added to the set and vice versa

a = [1, 2, 3, 1, 2, 3, 4, 5, 6]
b = set(a)
print(a)
print(b)
b.add(9)
print(a)
print(b)
a.append(10)
print(a)
print(b)