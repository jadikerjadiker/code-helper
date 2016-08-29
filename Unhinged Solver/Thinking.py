'''
I have a method to solve these by brute force (as I think most people pretty much do to solve these anyway)
Hexagonal coordinate system, as described here (http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/).
First, generate all the possible situations:
There are 9 hinges you can flip (or not flip). So there are 2^9 = 1024 different ways to flip.
Then double that because you can view the result from the top or from the bottom.
Each situation can be represented as a list with each piece being a tuple of coordinates as an index and each value being 0 (white) or 1 (black).
Then, you can orient each situation so that the piece with the most negative first coordinate and then most negative second coordinate ends up at (0, 0), transposing the rest with it.
This list is called a situation. It would look something like [(0, 0):0, (1, 0):1, (1, 2): 0, ...]

Each situation is made by flipping hinges, so those hinges are represented by their numbers (as you would see in the solution).
Then, the situation can be preceded by a 0, if viewed from the top, or a 1, if viewed from the bottom.
For example (1, 3, 6) would represent the solution (3, 6) when viewed from the bottom.
This is called a possible solution. It would look something like this (1, 1, 4, 6, 8, 9). It is always sorted (except for the first digit) by numerical order.
So the dictionary of all the possible solutions should look like {(1, 1, 4, 6, 8, 9):[(0, 0):0, (1, 0):1, (1, 2): 0, ...], ...}
with 2048 values in it.

Then, we create the 6 rotations of the actual solution (with the lower one in the bottom left) and store it in a dictionary.

Then, we see if any of the possible solutions match any of the rotations in the solution dictionary.

If they are, that one's a winner.
'''