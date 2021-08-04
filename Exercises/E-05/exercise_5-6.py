"""
Exercise 5-6

The Koch curve is a fractal that looks something like Figure 5-2. To draw a Koch curve with length x, all you have to do is:

1. Draw a Koch curve with length x/3.
2. Turn left 60 degrees.
3. Draw a Koch curve with length x/3.
4. Turn right 120 degrees.
5. Draw a Koch curve with length x/3.
6. Turn left 60 degrees.
7. Draw a Koch curve with length x/3.

The exception is if x is less than 3: in that case, you can just draw a straight line with length x.

1. Write a function called koch that takes a turtle and a length as parameters, and that uses the turtle to draw a Koch curve with the given length.

2. Write a function called snowflake that draws three Koch curves to make the outline of a snowflake. Solution: http://thinkpython2.com/code/koch.py.

3. The Koch curve can be generalized in several ways. See http://en.wikipedia.org/ wiki/Koch_snowflake for examples and implement your favorite.

"""

def koch(t, x):
    # base case
    if x < 6:
        t.fd(x)
        return

    koch(t, x/3)

    t.lt(60)
    koch(t, x/3)

    t.rt(120)
    koch(t, x/3)

    t.lt(60)
    koch(t, x/3)


def snowflake(t, length):
    t.lt(60)
    for _ in range(3):
        koch(t, length)
        t.rt(120)
    t.rt(60)


import turtle

bob = turtle.Turtle()
bob.speed(2000)

bob.pu()
bob.goto(-150, -75)
bob.pd()
snowflake(bob, 300)

# koch_fun(bob, 20)

turtle.mainloop()
