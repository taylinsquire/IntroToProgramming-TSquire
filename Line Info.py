
from graphics import *
import math

win = GraphWin("Line Segment Info", 480, 340)
win.setCoords(0, 0, 100, 100)

bText = Text(Point(50, 5), "Click twice to create a line.")
bText.draw(win)

p1 = win.getMouse()
p1.draw(win)
p2 = win.getMouse()
p2.draw(win)

line = Line(p1, p2)
line.draw(win)

mid = line.getCenter()
mid.setFill("cyan")
mid.draw(win)

dx = line.getP1().getX() - line.getP2().getX()
dy = line.getP1().getY() - line.getP2().getY()
pDx = (dx/100) * win.getWidth()
pDy = (dy/100) * win.getHeight()

slope = dy/dx
pixelLength = math.sqrt(pDx**2 + pDy**2)

Text(Point(50, 90), "Length: " + str(pixelLength)).draw(win)
Text(Point(50, 95), "Slope: " + str(slope)).draw(win)
bText.setText("Click again to quit.")

win.getMouse()
