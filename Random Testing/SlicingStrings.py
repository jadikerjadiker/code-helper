#Yes, the last number in a slice can be one higher than the possible index of the string.
#it returns the substring right up to (but not including) the second index given
#if the two indexes are the same it gives an empty string

a = "h"
b = a[0:1]
print(b)

a = "abcde"
print(a[:3])
print(a[1:1], a[1:2])