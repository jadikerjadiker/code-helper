'''
I want to find all sets of numbers {n, m}
such that 

(((n + m)%10 +or- 1)%10 + (n + m)%10)%10 = m

where m and n are non-negative integers less than 10.

And I want it to print out the sets as {n, m, (n+m)%10, ((n+m)%10 +or- 1)%10}
where of course (n+m%10 +or- 1)%10 = (n+m +or- 1)%10
'''

'''
Reasoning:

My grandpa used to make these "Number Mazes" for me, where all the numbers in the maze were non-negative integers less than 10.

Here's a given board. You always start in the top left and try to get to the bottom right.

3---5---8
|   |   |
4---5---7
|   |   |
3---0---5
|   |   |
7---1---2


To get from one spot to another, there are a coupld ways to move.
Note: Diagonals never count. They are not adjacent. You can't interact with them during a move.
The two ways you can move are:
1. If you are on a number with a value of n, you can move to any adjacent number with value (n +or- 1)%10.
This means that if I'm on either of the 3's, I can move to the 4, or if I'm on the 8 I can move to the adjacent 7

2. If you are on a number with a value of n, and an adjacent number has a value of m,...
then you can hop directly over m fron n and go to a space with value (n+m)%10
For example, I can jump from the 3 in the top left to the 8 because (3+5)%10=8, or from the 4 to the 7 because (4+3)%10=7,
or from the top middle 5 to the 0 because (5+5)%10=0

To solve the puzzle above, you go from the 3, hop over the 5 to the 8. Then, from the 8 to the 7. Then hop over the 5 to get to the 2.

Let's say we have a board where the numbers represent positions (so I can describe movement more easily)

*1--*2--*3--*4
 |   |   |   |
*5--*6--*7--*8


So the Stone Sets (named after my grandpa, Bruce Stone) {n, m, (n+m)%10, ((n+m)%10 +or- 1)%10} ...
are interesting in the game because if positions 1, 2, 3, 4 were a Stone Set {value at 1, value at 2, value at 3, value at 4}...
then we would be able to

Start at position 1
Jump to 3 (hop over 2)
Move to 4 (plus or minus 1 rule)
Jump to 2 (hop over 3)

So while we're moving many times, it only makes a difference in one position.
This type of pattern can also be very difficult for a player to detect.
Bruce Stone called them "Golden Cascades" because they look like the juggling move called the "cascade".
'''

import itertools

posses = itertools.product(range(10), range(10)) #all the possible values for n and m in a list

solNum = 0 #the number of Stone Sets that have been found.
for pair in posses:
    lastnum = None
    n, m = pair
    #things I don't want to be true because then the "plus or minus rule" allows you to not do the jumps
    #need to check 9 as well because "one away" is (10 +or- 1) which is (1 or 9), not just 1
    if not (abs(n-m)==1 or abs(n-m)==9 or n==1 or n==9):
        if (((n + m)%10 + 1)%10 + (n + m)%10)%10 == m:
            lastnum = ((n + m)%10 + 1)%10 #the one that depends on the plus or minus
        if (((n + m)%10 - 1)%10 + (n + m)%10)%10 == m:
            lastnum = ((n + m)%10 - 1)%10 #the one that depends on the plus or minus
        if isinstance(lastnum, (int, long)): 
            solNum+=1
            print("{}. ".format(solNum)+"{"+"{}, {}, {}, {}".format(n, m, (n+m)%10, lastnum)+"}")

'''
Output:

1. {2, 5, 7, 8}
2. {2, 7, 9, 8}
3. {3, 3, 6, 7}
4. {3, 5, 8, 7}
5. {4, 1, 5, 6}
6. {5, 1, 6, 5}
7. {5, 9, 4, 5}
8. {6, 9, 5, 4}
9. {7, 5, 2, 3}
10. {7, 7, 4, 3}
11. {8, 3, 1, 2}
12. {8, 5, 3, 2}
'''