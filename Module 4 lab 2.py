"""
CTEC 121
Matthew Bly
Module 4 Lab 1
Code for module 4 lab 1
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import *
def main():
    '''
    # demonstratinon of answer to problem 17 from module 3 quiz
    startValue = 1
    endValue = 10
    sum = 0
    if startValue % 2 == 1:
        startValue = startValue + 1
    for i in range(startValue, endValue, 2):
        sum = sum + i
    print(sum)
    '''
    win =GraphWin("demo", 800, 800)
    win.setCoords(-4.0, -4.0, 4.0, 4.0)
    p1 = Circle(Point(2, 3), 5)
    p1.setFill("red")
    p1.draw(win)
    p2 = Point(-3, 1).draw(win)
    p3 = Point(-1.5, -2.5).draw(win)

    input()
    
main()    