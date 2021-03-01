# james jack
# 2/24/21

# Problem 6: Use the polygon program from the last module and convert it to a function.

import turtle


def polygon(t, side):  # creates func of base shape
    for i in range(6):  # makes turtle make shapes at 60 degree angle
        t.forward(side)
        t.left(60)


# creates window
wn = turtle.Screen()
james = turtle.Turtle()
james.color("hot pink")
james.pensize(5)

# loops the creation of the shapes at angles
for x in range(10):
    polygon(james, 90)
    james.right(360 / 10)  # creates the polygon by moving in space of 360 degrees to make a circle

# this one was alot of trial and error!

wn.exitonclick()
