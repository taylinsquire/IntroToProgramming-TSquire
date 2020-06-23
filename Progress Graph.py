
from graphics import *

win = GraphWin("Progress Graph", 480, 100)
win.setCoords(0, 0, 100, 100)

backBar = Rectangle(Point(20, 35), Point(80, 65))
backBar.setFill("gray")
backBar.draw(win)

days = int(input("Enter the number of days the student has been in their course: "))
assignments = int(input("Enter the number of assignments the student has completed: "))

progress = assignments / days

percent = Text(backBar.getCenter(), str(progress * 100) + "%")

barLength = progress * 60

bar = Rectangle(Point(20, 35), Point(20 + barLength, 65))
bar.setFill("green")
bar.draw(win)
percent.draw(win)

win.getMouse()
