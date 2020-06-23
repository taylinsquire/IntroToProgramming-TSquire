
from graphics import *

win = GraphWin("Dice")
win.setCoords(0, 0, 100, 100)

die1 = Rectangle(Point(5, 45), Point(15, 55))

die2 = die1.clone()
die2.move(20, 0)

die3 = die2.clone()
die3.move(20, 0)

die4 = die3.clone()
die4.move(20, 0)

die5 = die4.clone()
die5.move(20, 0)

die1.draw(win)
die2.draw(win)
die3.draw(win)
die4.draw(win)
die5.draw(win)

dice = [die1, die2, die3, die4, die5]
num = 1
for i in dice:
    Text(i.getCenter(), str(num)).draw(win)
    num += 1


win.getMouse()