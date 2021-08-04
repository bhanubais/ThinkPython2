"""
The following exercises use the turtle module, described in Chapter 4

Exercise 5-5

Read the following function and see if you can figure out what it does (see the examples in Chapter 4). Then run it and see if you got it right.

"""

def draw(t, length, n):
    if n == 0:
        return
    angle = 90
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


import turtle

bob = turtle.Turtle()

draw2(bob, 10, 4)

turtle.mainloop()

# ANSWER
# Creating two branch tree recursively
