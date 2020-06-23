
from graphics import *

win = GraphWin("Five-click House", 480, 340)
win.setCoords(0, 0, 100, 100)

inst = Text(Point(50, 5), "Click twice to create the frame of the house.")
inst.draw(win)

p1 = win.getMouse()
p1.draw(win)
p2 = win.getMouse()
p2.draw(win)

house = Rectangle(p1, p2)
house.setFill("brown")
house.draw(win)
houseWidth = abs(house.getP1().getX()-house.getP2().getX())
houseHeight = abs(house.getP1().getY()-house.getP2().getY())

inst.setText("Click to choose the center of the top of the door.")

doorCenter = win.getMouse()
doorWidth = houseWidth / 5
if house.getP2().getY() < house.getP1().getY():
    doorHeight = doorCenter.getY() - house.getP2().getY()
else:
    doorHeight = doorCenter.getY() - house.getP1().getY()

door = Rectangle(Point(doorCenter.getX() - doorWidth / 2, doorCenter.getY()), Point(doorCenter.getX() + doorWidth / 2, doorCenter.getY() - doorHeight))
door.setFill("White")
door.draw(win)

inst.setText("Click to choose the center point of the window.")
windowCenter = win.getMouse()
windowWidth = doorWidth / 2
windowHeight = 3 / 2 * windowWidth

window = Rectangle(Point(windowCenter.getX() - windowWidth / 2, windowCenter.getY() - windowHeight / 2), Point(windowCenter.getX() + windowWidth / 2, windowCenter.getY() + windowHeight / 2))
window.setFill("White")
window.draw(win)

inst.setText("Click to choose where to put the peak of the roof.")
roof = Polygon(Point(house.getCenter().getX() - houseWidth / 2, house.getCenter().getY() + houseHeight / 2), Point(house.getCenter().getX() + houseWidth / 2, house.getCenter().getY() + houseHeight / 2), win.getMouse())
roof.setFill("Black")
roof.draw(win)

win.getMouse()
