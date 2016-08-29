'''
The goal of this is to test to see if I can
1. Write a class into a file
2. Import that file
3. Create and instance of that class
4. Have that instance run a particular method that prints something out.
5. Change the class (add a new method to it)
6. Reimport the file
7. See if I can run the new method on a new instance of the class and have it print something.

It works! Making this code helper in Python may have just been made so much easier for me!
'''

with open("TheModule.py", "w") as f:
    sentinel = '...'
    myInput = '\n'.join(iter(raw_input, sentinel))
    f.write(myInput)

import TheModule as tm

me = tm.MyClass()
me.sayHi()

with open("TheModule.py", "w") as f:
    sentinel = '...'
    myInput = '\n'.join(iter(raw_input, sentinel))
    f.write(myInput)

reload(tm)

me = tm.MyClass()
me.sayBye()
    