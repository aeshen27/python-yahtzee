#Abby Shen
#
#this module contains my score cell class


class ScoreCell:
    """Score cell class. Returns value for given Yahtzee category."""
    def __init__(self, value1, value2, value3, value4, value5):
        #assign instance variables
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        self.value5 = value5
        #self.one, self.two, self.three, etc. count the number of times that
        #value appears out of the five given values
        #starts at 0 and adds one for every matching value it comes across
        self.one = 0
        if self.value1 == 1:
            self.one += 1
        if self.value2 == 1:
            self.one += 1
        if self.value3 == 1:
            self.one += 1
        if self.value4 == 1:
            self.one += 1
        if self.value5 == 1:
            self.one += 1
        self.two = 0
        if self.value1 == 2:
            self.two += 1
        if self.value2 == 2:
            self.two += 1
        if self.value3 == 2:
            self.two += 1
        if self.value4 == 2:
            self.two += 1
        if self.value5 == 2:
            self.two += 1
        self.three = 0
        if self.value1 == 3:
            self.three += 1
        if self.value2 == 3:
            self.three += 1
        if self.value3 == 3:
            self.three += 1
        if self.value4 == 3:
            self.three += 1
        if self.value5 == 3:
            self.three += 1
        self.five = 0
        if self.value1 == 5:
            self.five += 1
        if self.value2 == 5:
            self.five += 1
        if self.value3 == 5:
            self.five += 1
        if self.value4 == 5:
            self.five += 1
        if self.value5 == 5:
            self.five += 1
        self.four = 0
        if self.value1 == 4:
            self.four += 1
        if self.value2 == 4:
            self.four += 1
        if self.value3 == 4:
            self.four += 1
        if self.value4 == 4:
            self.four += 1
        if self.value5 == 4:
            self.four += 1
        self.six = 0
        if self.value1 == 6:
            self.six += 1
        if self.value2 == 6:
            self.six += 1
        if self.value3 == 6:
            self.six += 1
        if self.value4 == 6:
            self.six += 1
        if self.value5 == 6:
            self.six += 1
        

    def ones(self):
        """returns score in "Ones" category"""
        #returns the number of ones
        score = self.one
        return(score)

    def twos(self):
        """returns score in "Twos" category"""
        #returns the number of twos times two to get the score
        score = self.two * 2
        return(score)

    def threes(self):
        """returns score in "Threes" category"""
        #returns the number of threes times three to get the score
        score = self.three * 3
        return(score)

    def fours(self):
        """returns score in "Fours" category"""
        #returns the number of fours times four to get the score
        score = self.four * 4
        return(score)

    def fives(self):
        """returns score in "Fives" category"""
        #returns the number of fives times five to get the score
        score = self.five * 5
        return(score)

    def sixes(self):
        """returns score in "Sixes" category"""
        #returns the number of sixes times six to get the score
        score = self.six * 6
        return(score)

    def yahtzee(self):
        """returns score in "Yahtzee" category"""
        score = 0
        #if all the values are the same, return 50 as the score
        #otherwise, 0 is returned as the score
        if self.value1 == self.value2 == self.value3 == self.value4 == self.value5:
            score = 50
        return(score)

    def chance(self):
        """returns score in "Chance" category"""
        #returns the sum of all the values
        score = self.value1 + self.value2 + self.value3 + self.value4 + self.value5
        return(score)

    def threekind(self):
        """returns score in "Three of a Kind" category"""
        #if there are three or more of any number, return the sum of the values
        #otherwise return 0 as the score
        score = 0
        if self.one >= 3 or self.two >= 3 or self.three >= 3 or self.four >= 3 or self.five >= 3 or self.six >= 3:
            score = self.value1 + self.value2 + self.value3 + self.value4 + self.value5
        return(score)

    def fourKind(self):
        """returns score in "Four of a Kind" category"""
        #if there are four or more of any number, return the sum of the values
        #otherwise return 0 as the score
        score = 0
        if self.one >= 4 or self.two >= 4 or self.three >= 4 or self.four >= 4 or self.five >= 4 or self.six >= 4:
            score = self.value1 + self.value2 + self.value3 + self.value4 + self.value5
        return(score)

    def largeStraight(self):
        """returns score in "Large Straight" category"""
        #if there is one of each value 1-5 OR if there is one of each value
        #2-6, return 40 as the score, otherwise 0
        score = 0
        if self.one == self.two == self.three == self.four == self.five == 1:
            score = 40
        elif self.six == self.two == self.three == self.four == self.five == 1:
            score = 40
        return(score)
            
    def smallStraight(self):
        """returns score in "Small Straight" category"""
        #if there is one or more of each value 1-4 OR 2-5 OR 3-6, return 30
        #as the score, otherwise 0
        score = 0
        if self.one >= 1 and self.two >= 1 and self.three >= 1 and self.four >= 1:
            score = 30
        elif self.five >= 1 and self.two >= 1 and self.three >= 1 and self.four >= 1:
            score = 30
        elif self.five >= 1 and self.six >= 1 and self.three >= 1 and self.four >= 1:
            score = 30
        return(score)

    def fullHouse(self):
        """returns score in "Full House" category"""
        #if there is three of one number and two of another, return 25 as the
        #score, otherwise return 0
        score = 0
        if self.one == 3 or self.two == 3 or self.three == 3 or self.four == 3 or self.five == 3 or self.six == 3:
            if self.one == 2 or self.two == 2 or self.three == 2 or self.four == 2 or self.five == 2 or self.six == 2:
                score = 25
        return(score)

        
