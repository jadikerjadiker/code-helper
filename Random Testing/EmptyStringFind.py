#so it doesn't throw an error if a is empty
#and it does find nothing at 0 in an empty string (or any string, really)

import string
a = ""
print(string.find(a, "1"))
print(string.find(a, ""))
print(string.find("abcdef", ""))