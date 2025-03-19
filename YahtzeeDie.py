#Abby Shen
#
#This module contains my die class

from graphics import *
from random import randrange

#win = GraphWin("test window", 600, 600)
#win.setBackground("white")

class Die:
    """Die class. Creates a six sided die that can be rolled."""
    def __init__(self, win, center, sideLength):
        #define instance variables
        self.win = win
        self.center = center
        self.sideLength = float(sideLength)
        #get x and y components of the center point
        self.centerX = self.center.getX()
        self.centerY = self.center.getY()
        #use x and y components of the center to find x and y components of the
        #opposite corners of the die
        self.x1 = self.centerX - (self.sideLength/2)
        self.y1 = self.centerY + (self.sideLength/2)
        self.x2 = self.centerX + (self.sideLength/2)
        self.y2 = self.centerY - (self.sideLength/2)
        #use those to make corner points
        point1 = Point(self.x1, self.y1)
        point2 = Point(self.x2, self.y2)
        #use corner points to make the square, set color to white and draw
        self.die = Rectangle(point1, point2)
        self.die.setFill("white")
        self.die.draw(self.win)
        #side length divided by 15 to get a proportional dot radius
        self.dotrad = self.sideLength/15
        #initial value of the die is 1
        self.val = 1
        #draw a single dot in the middle to display the starting value of 1
        self.oneDot = Circle(self.center, self.dotrad)
        self.oneDot.setFill("black")
        self.oneDot.draw(self.win)
        #die starts active (rollable)
        self.active = True

    #these number methods won't be directly used in my Yahtzee lab, but used within
    #a subsequent method
    #each number method creates the "look" for a certain number with dots
    def one(self):
        self.oneDot.draw(self.win)

    def two(self):
        self.twoDot1 = Circle(Point(self.centerX - (self.sideLength/4), self.centerY + (self.sideLength/4)), self.dotrad)
        self.twoDot1.setFill("black")
        self.twoDot1.draw(self.win)
        self.twoDot2 = Circle(Point(self.centerX + (self.sideLength/4), self.centerY - (self.sideLength/4)), self.dotrad)
        self.twoDot2.setFill("black")
        self.twoDot2.draw(self.win)

    def three(self):
        self.threeDot1 = Circle(Point(self.centerX - (self.sideLength/4), self.centerY + (self.sideLength/4)), self.dotrad)
        self.threeDot1.setFill("black")
        self.threeDot1.draw(self.win)
        self.threeDot2 = Circle(Point(self.centerX + (self.sideLength/4), self.centerY - (self.sideLength/4)), self.dotrad)
        self.threeDot2.setFill("black")
        self.threeDot2.draw(self.win)
        self.threeDot3 = Circle(self.center, self.dotrad)
        self.threeDot3.setFill("black")
        self.threeDot3.draw(self.win)

    def four(self):
        self.fourDot1 = Circle(Point(self.centerX - (self.sideLength/4), self.centerY + (self.sideLength/4)), self.dotrad)
        self.fourDot1.setFill("black")
        self.fourDot1.draw(self.win)
        self.fourDot2 = Circle(Point(self.centerX + (self.sideLength/4), self.centerY - (self.sideLength/4)), self.dotrad)
        self.fourDot2.setFill("black")
        self.fourDot2.draw(self.win)
        self.fourDot3 = Circle(Point(self.centerX - (self.sideLength/4), self.centerY - (self.sideLength/4)), self.dotrad)
        self.fourDot3.setFill("black")
        self.fourDot3.draw(self.win)
        self.fourDot4 = Circle(Point(self.centerX + (self.sideLength/4), self.centerY + (self.sideLength/4)), self.dotrad)
        self.fourDot4.setFill("black")
        self.fourDot4.draw(self.win)

    def five(self):
        self.fiveDot1 = Circle(Point(self.centerX - (self.sideLength/4), self.centerY + (self.sideLength/4)), self.dotrad)
        self.fiveDot1.setFill("black")
        self.fiveDot1.draw(self.win)
        self.fiveDot2 = Circle(Point(self.centerX + (self.sideLength/4), self.centerY - (self.sideLength/4)), self.dotrad)
        self.fiveDot2.setFill("black")
        self.fiveDot2.draw(self.win)
        self.fiveDot3 = Circle(Point(self.centerX - (self.sideLength/4), self.centerY - (self.sideLength/4)), self.dotrad)
        self.fiveDot3.setFill("black")
        self.fiveDot3.draw(self.win)
        self.fiveDot4 = Circle(Point(self.centerX + (self.sideLength/4), self.centerY + (self.sideLength/4)), self.dotrad)
        self.fiveDot4.setFill("black")
        self.fiveDot4.draw(self.win)
        self.fiveDot5 = Circle(self.center, self.dotrad)
        self.fiveDot5.setFill("black")
        self.fiveDot5.draw(self.win)

    def six(self):
        self.sixDot1 = Circle(Point(self.centerX - (self.sideLength/4), self.centerY + (self.sideLength/4)), self.dotrad)
        self.sixDot1.setFill("black")
        self.sixDot1.draw(self.win)
        self.sixDot2 = Circle(Point(self.centerX + (self.sideLength/4), self.centerY - (self.sideLength/4)), self.dotrad)
        self.sixDot2.setFill("black")
        self.sixDot2.draw(self.win)
        self.sixDot3 = Circle(Point(self.centerX - (self.sideLength/4), self.centerY - (self.sideLength/4)), self.dotrad)
        self.sixDot3.setFill("black")
        self.sixDot3.draw(self.win)
        self.sixDot4 = Circle(Point(self.centerX + (self.sideLength/4), self.centerY + (self.sideLength/4)), self.dotrad)
        self.sixDot4.setFill("black")
        self.sixDot4.draw(self.win)
        self.sixDot5 = Circle(Point(self.centerX - (self.sideLength/4), self.centerY), self.dotrad)
        self.sixDot5.setFill("black")
        self.sixDot5.draw(self.win)
        self.sixDot6 = Circle(Point(self.centerX + (self.sideLength/4), self.centerY), self.dotrad)
        self.sixDot6.setFill("black")
        self.sixDot6.draw(self.win)

    def roll(self):
        """rolls the die, both returning and visually expressing the value"""
        if self.active: #only rollable if the die is active
            self.clear() #clears anything already on it, method defined below
            #randomly shuffles the face 5 times to look like it is "rolling"
            #(sort of)
            for i in range(5):
                #get random value from 1-6
                self.val = randrange(1, 7)
                #depending on the value, call method to display the dots
                if self.val == 1:
                    self.one()
                elif self.val == 2:
                    self.two()
                elif self.val == 3:
                    self.three()
                elif self.val == 4:
                    self.four()
                elif self.val == 5:
                    self.five()
                elif self.val == 6:
                    self.six()
                #clear before displaying the final "rolled" value
                self.clear()
            #get random value, this one is the real one
            self.val = randrange(1, 7)
            #same idea as above
            if self.val == 1:
                self.one()
            elif self.val == 2:
                self.two()
            elif self.val == 3:
                self.three()
            elif self.val == 4:
                self.four()
            elif self.val == 5:
                self.five()
            elif self.val == 6:
                self.six()
            #return the value
            return(self.val)

    def clear(self):
        """clears the dots displayed on the die face"""
        #undraws all dots depending on what the current die value is
        if self.val == 1:
            self.oneDot.undraw()
        elif self.val == 2:
            self.twoDot1.undraw()
            self.twoDot2.undraw()
        elif self.val == 3:
            self.threeDot1.undraw()
            self.threeDot2.undraw()
            self.threeDot3.undraw()
        elif self.val == 4:
            self.fourDot1.undraw()
            self.fourDot2.undraw()
            self.fourDot3.undraw()
            self.fourDot4.undraw()
        elif self.val == 5:
            self.fiveDot1.undraw()
            self.fiveDot2.undraw()
            self.fiveDot3.undraw()
            self.fiveDot4.undraw()
            self.fiveDot5.undraw()
        elif self.val == 6:
            self.sixDot1.undraw()
            self.sixDot2.undraw()
            self.sixDot3.undraw()
            self.sixDot4.undraw()
            self.sixDot5.undraw()
            self.sixDot6.undraw()
        
    def clicked(self, point):
        """returns True if die is active and clicked"""
        #if the die is active and the point is within the range of the die rectangle,
        #returns true
        return (self.active and
                self.x1 <= point.getX() <= self.x2 and
                self.y2 <= point.getY() <= self.y1)
    #activate die
    def activate(self):
        self.active = True
    #deactivate die
    def deactivate(self):
        self.active = False
    #return die value
    def getVal(self):
        return(self.val)
    #set line weight for border
    def setWidth(self, pixels):
        self.die.setWidth(pixels)
    

#die = Die(win, Point(300, 300), 30)
#die.roll()

        

    
        
