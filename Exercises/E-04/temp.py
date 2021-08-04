from polygon import arc
import turtle

def spiral(t, c = 10, n = 5, m = 1, a = 180, type='linear'):
    """create a spiral
    t : Turtal object
    c : starting radius
    n : number of rounds
    m: by this amount radius will increase
    a : angle when it increase it's radius
    type: linear | exponential | hyperbolic
    """
    # number of rounds based on provided angle
    n = n * round(360/abs(a))

    if type == 'linear':
        key_fun = lambda m, x, c: m*x + c
    elif type == 'exponential':
        key_fun = lambda m, x, c: m*x**2 + c
    elif type == 'hyperbolic':
        key_fun = lambda m, x, c: a / (x + 1)
    else:
        print('Unknown spiral type.')
        print('Type: linear | exponential | hyperbolic')
        return

    r = None
    for x in range(n):
        print(f'r = {r}')
        r = key_fun(m, x, c)
        arc(t, r, a)


bob = turtle.Turtle()

# Linear spiral
# spiral(bob, 5, 3, 5, 90)
# spiral(bob, 5, 3, 5, -90)

# Exponential spiral
# spiral(bob, 3, 3, 2, 90, 'exponential')

# hyperbolic
# spiral(t = bob, n = 5, a = 180, type = 'hyperbolic')

spiral(bob, 5, 3, 5, 90)
spiral(bob, 60, 3, -5, -90)


# wait for the user to close the window
bob.hideturtle()
turtle.mainloop()
