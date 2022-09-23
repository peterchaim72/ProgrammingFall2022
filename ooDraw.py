# OODraw.py  (Object Oriented Drawing Tool)
#
# This class wraps a Python turtle to provide functions
# that are useful for drawing. The calling code
# does not need to know anything about turtles.
#
# 9/15/2022 Peter Weinstein

import turtle


class OODraw:

    # initialize a Python turtle to use for drawing.
    # the coordinates identify a rectangle within which a click
    # will be recognized as being a click on this object.
    # warning: the smaller coordinate must be the "from" value
    def __init__(self, name, fromX, toX, fromY, toY):
        self.name = name
        self.fromX = fromX
        self.toX = toX
        self.fromY = fromY
        self.toY = toY
        self.tess = turtle.Turtle()
        self.turtle = turtle
        print(name + " recognizes itself within: x1=" + str(self.fromX) +
              " x2=" + str(self.toX) + " y1=" + str(self.fromY) + " y2=" +
              str(self.toY))
        return

    # draw a square starting at a given angle
    def draw_square(self, x, y, angle, length):
        self.tess.setheading(angle)
        for i in range(4):
            self.tess.forward(length)
            self.tess.right(90)
        return

    # determines whether the click is within the boundaries defined
    # for this instance of ooDraw.
    # returns True/False, whether a click is for this object instance
    def recognize_click(self, clickX, clickY):
        is_me = (clickX >= self.fromX and clickX <= self.toX
                 and clickY >= self.fromY and clickY <= self.toY)
        if is_me:
            print(self.name + ": click at x=" + str(clickX) + " y=" +
                  str(clickY) + " is for me")
        else:
            print(self.name + ": click at x=" + str(clickX) + " y=" +
                  str(clickY) + " is not for me")
        return

    # tell Python to execute the recognize_click() function
    # when the user clicks the mouse
    def bindOnClick(self, screen):
        screen.onclick(self.recognize_click, add=True)
        return
