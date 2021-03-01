# james jack
# 2/24/21


# Problem 5: Use the following chunk of code as a base to produce the image shown below.

import turtle


def multi_square(t, sz):  # creates func with param t for turtl and sz for size
    for i in range(4):  # creates square sides
        t.forward(sz)  # move turtle forwards in regards to sze input
        t.left(90)  # creates square


wn = turtle.Screen()  # creates background and screen

james = turtle.Turtle()  # creates turtle named james with blue
james.color("blue")
james.pensize(3)

size = 15  # size
for x in range(5):  # create multiple squares
    multi_square(james, size)  # calls function of making squares
    size = size + 20  # size increases to make them be made outwards
    james.up()  # tells the turtle the directions to take to make the squares correctly as it makes each one
    james.backward(10)
    james.right(90)
    james.forward(10)
    james.left(90)
    james.down()

wn.exitonclick()
