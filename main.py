# main.py  (using our Object Oriented Drawing Tool)
#
# Event-driven object-oriented exercise where drawn objects
# respond to mouse clicks.
#
# 9/23/2022 Peter Weinstein. Created exercise for students.
# < date >  < your name >. < what you did >

import turtle
from ooDraw import OODraw

# initialize graphics output window
screen = turtle.Screen()
screen.setup(500, 400)
# instantiate two drawing tools
draw = OODraw("draw1", 0, 100, 0, 100)
draw.bindOnClick(screen)

draw2 = OODraw("draw2", 0, 100, -100, 0)
draw2.bindOnClick(screen)

# draw two squares that clicks within their boundaries
draw.draw_square(0, 0, 90, 100)
draw2.draw_square(0, 0, 0, 100)

# --------------- exercise steps -----------------------------
#
# 1. Copy functions from your Turtles program to ooDraw.py, including
#    draw_square(), draw_rectangle(), set_location(), and any
#    others that would be generally useful for a drawing tool.
#
#    Adapt the functions for object oriented use (adding "self"
#    as an argument, and using self to reference the turtle "tess").
#
#    Note, using these functions should NOT require knowledge of turtles.
#
# 2. In main.py, instantiate four instances of OODraw, one for
#    each element of the house drawing including wall, window, door, roof.
#    Now use these four objects to draw your house, with each drawing
#    just one element.
#
# 3. Now use the "event listening" already coded to take appropriate
#    action when the user clicks on a window or a door. For example,
#    you might redraw the window/door to toggle whether it is open
#    or closed.
#

# respond to events until the program is stopped
turtle.mainloop()
