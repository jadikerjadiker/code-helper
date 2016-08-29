#Made in 2015 by London Lowmanstone IV
#defines how to compute different directions
#0 is up, and it goes clockwise from there, so 2 is down

#return the next direction clockwise from the one given
def dirC(num):
    return (num+1)%4

#return the next direction counter-clockwise from the one given
def dirCc(num):
    return (num-1)%4

#return the direction opposite the one given
def dirOpp(num):
    return (num+2)%4
