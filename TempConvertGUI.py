
from graphics import *

win = GraphWin("Temperature Converter")
win.setBackground("tan")

Text(Point(50, 75), "Celsius:").draw(win)
Text(Point(50, 150), "Fahrenheit:").draw(win)
inputText = Entry(Point(100, 75), 5)
inputText.setText("0.0")
inputText.draw(win)
outputText = Text(Point(100, 150), "")
outputText.draw(win)
button = Text(Point(100, 180), "Convert")
button.draw(win)
Rectangle(Point(75, 165), Point(125, 195)).draw(win)

win.getMouse()

celsius = float(inputText.getText())
fahrenheit = 9/5 * celsius + 32

outputText.setText(round(fahrenheit, 2))
button.setText("Quit")

win.getMouse()

