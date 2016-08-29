'''
London Lowmanstone IV
InputParser Class
Version 1.0
2/19/2016
'''

'''
This class takes a string and a format file object.

This class will use the format file object to convert the string (input) into a list of two lists.

The first list will be a list of all the phrases it found inside the input.
The second list is a list of numbers which correspond to the index of the phrases inside the first list.
The second list will show the order of the phrases as they actually occur in the input.
This gives both a list of all the needed phrases, as well as how to put the phrases together (what should be passed as a parameter to what)

Here's an example to help clear things up:
Input: "if the user has candy then make the boy happy"
Could give back (assuming these are the defined phrases):
[
    ["if...then...", "the user has...", "candy", "make the boy...", "happy"],
    [0, 1, 2, 1, 3, 4]
]

Where "..." is the "Parameter Slot Symbol" item in the file. If there is none, it defaults to "...".
'''

'''
More details as to how this will work here:
More in depth overview:
The parser will also todo talk about the Do Not Parse Symbol thing
'''