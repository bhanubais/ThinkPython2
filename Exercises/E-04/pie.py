from math import sin, pi
import turtle

def pie(t, radius, n):
    """Creates a n-sided pie of given radius
    """
    # central angle (angle of each flap)
    c_angle = 360 / n
    # side length of polygone
    side_len = 2 * radius * sin(pi / n)

    # initial angle
    t.lt(c_angle / 2)

    for _ in range(n):
        t.fd(radius)
        t.lt(90 + c_angle / 2)
        t.fd(side_len)
        t.lt(90 + c_angle / 2)
        t.fd(radius)
        t.lt(180)

    # reset angle
    t.lt(- c_angle / 2)


def move(t, distance):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(distance)
    t.pd()


bob = turtle.Turtle()

move(bob, -150)
pie(bob, 50, 5)

move(bob, 150)
pie(bob, 50, 6)

move(bob, 150)
pie(bob, 50, 7)



# wait for the user to close the window
turtle.mainloop()