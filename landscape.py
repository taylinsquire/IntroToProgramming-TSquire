
from graphics import *

win = GraphWin()

land = Rectangle(Point(0, 180), Point(199, 199))
land.setFill("green")
land.setOutline("green")

air = Rectangle(Point(0, 0), Point(199, 199))
air.setFill("skyblue")
air.setOutline("skyblue")

sun = Circle(Point(30, 30), 15)
sun.setFill("yellow")
sun.setOutline("yellow")

house = Rectangle(Point(120, 180), Point(180, 120))
house.setFill("Brown")

roof = Polygon(Point(110, 120), Point(house.getCenter().getX(), 100), Point(190, 120))
roof.setFill("brown")

houseFull = [house, roof]

print(houseFull)

air.draw(win)
land.draw(win)
sun.draw(win)
house.draw(win)
roof.draw(win)

win.getMouse()
win.close()
