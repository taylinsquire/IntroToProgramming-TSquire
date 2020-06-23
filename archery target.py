
from graphics import *

win = GraphWin("Archery Target", 300, 300)
win.setCoords(0, 0, 200, 200)

center = Point(100, 100)
radius = 20

ring4 = Circle(center, radius * 5)
ring3 = Circle(center, radius * 4)
ring2 = Circle(center, radius * 3)
ring1 = Circle(center, radius * 2)
bullseye = Circle(center, radius)

ring4.setFill("white")
ring3.setFill("black")
ring2.setFill("blue")
ring1.setFill("red")
bullseye.setFill("yellow")

ring4.draw(win)
ring3.draw(win)
ring2.draw(win)
ring1.draw(win)
bullseye.draw(win)

win.getMouse()
