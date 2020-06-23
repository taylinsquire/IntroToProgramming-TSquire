
from graphics import *

principal = float(input("Please enter the principal value: "))
apr = float(input("Please enter the apr: "))

win = GraphWin("Investment Growth Chart", 320, 240)
win.setBackground("white")
Text(Point(20, 230), " 0.0 K").draw(win)
Text(Point(20, 180), " 2.5 K").draw(win)
Text(Point(20, 130), " 5.0 K").draw(win)
Text(Point(20, 80), " 7.5 K").draw(win)
Text(Point(20, 30), "10.0 K").draw(win)

height = principal * 0.02
bar = Rectangle(Point(40, 230), Point(65, 230 - height))
bar.setFill("green")
bar.setWidth(2)
bar.draw(win)

for year in range(1, 11):
    principal = principal * (1 + apr)
    xll = year * 25 + 40
    height = principal * 0.02
    bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

win.getMouse()
win.close()
