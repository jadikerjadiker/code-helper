'''
Things to keep track of:

How to split into graph:
Any point where two roads intersect or there's a house opening is a point.
The roads represent edges.

To win:
No collisions
All boxes delivered
No double-traveled edges
Trucks never pick up more than 3 boxes

Paths can be represented by points on the grid
To create a board, we can make a grid, type in the points that are connected, and then delete all the non-connected points.


Boxes on trucks, delivery
Time to move so that there are no collisions
Can't travel along the same edge, but can go at the same points.
Can't show up at the same point at the same time

Okay, so how do I want this thing to actually work? Random order of paths? permutations of houses to reach, permutations of boxes to pick up, permutations of all possible paths?
This is way too complicated for me to actually build out. I'd be better off fixing the lazer one.
'''