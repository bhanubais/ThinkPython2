import turtle
from math import pi
from polygon import *


def petal(t, r, angle):
    """Create a petal of radius r
    t     : Turtle object
    r     : radius (determines size of petal)
    angle : angle of one part of a petal
    """
    arc(t, r, angle)
    t.lt(180 - angle)
    arc(t, r, angle)
    t.lt(180 - angle)

def flower(t, r, n, angle):
    """create a flower of n petals
    n      : number of petals
    """
    petal_angle = 360 / n
    for _ in range(n):
        petal(t, r, angle)
        t.lt(petal_angle)

bob = turtle.Turtle()

# Flower 1
# flower(bob, 200, 7, 60)

# Flower 2
# flower(bob, 200, 10, 80)

# Flower 3
flower(bob, 200, 20, 24)


turtle.mainloop()