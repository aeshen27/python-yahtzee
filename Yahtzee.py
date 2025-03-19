#Abby Shen
#
#This module contains a single player Yahztee game

from graphics import *
from random import randrange
from Button import Button
from Die import Die
from ScoreCell import ScoreCell

def main():
    #making window for name entry
    startWin = GraphWin("Name Entry", 400, 300)
    startWin.setBackground("white")
    #prompt text and entry box
    namePrompt = Text(Point(200, 120), "Please enter your name:")
    namePrompt.draw(startWin)
    nameEntry = Entry(Point(200, 150), 8)
    nameEntry.draw(startWin)
    #start button to press after typing your name
    start = Button(startWin, Point(200, 180), 60, 15, "Start")
    #go is a variable used to see if the game is active or not, right now it is not because
    #the user has not pressed start yet
    go = False
    #activate start button
    start.activate()
    #while go is false, aka while the button has not been pressed yet, if the button is pressed
    #and the entry box is not empty, collect the name from the entry box, close the starting
    #window, and set go to true (to break the while loop)
    while not go:
        if start.clicked(startWin.getMouse()) and len(nameEntry.getText()) > 0:
            name = nameEntry.getText()
            startWin.close()
            go = True
    #the number of rounds and the user's high score are set to 0 before the large while loop
    #so that they don't reset after each round
    rounds = 0
    highScore = 0
    #while the game is active
    while go:
        #creating the game window with my favorite python color
        win = GraphWin("Game Window", 800, 600)
        win.setBackground("olive drab")
        #contructing and activating the quit button
        quitButton = Button(win, Point(750, 20), 40, 18, "Quit")
        quitButton.setFill("lightgray")
        quitButton.activate()
        #used stored name to display in the corner
        nameText = Text(Point(60, 20), name)
        nameText.setSize(13)
        nameText.draw(win)
        #text box (made of rectangle and text) to give the user basic instructions
        messageBox = Rectangle(Point(110, 175), Point(370, 225))
        messageBox.setFill("light gray")
        messageBox.draw(win)
        messageText = Text(Point(240, 200), "Press Roll to start game!")
        messageText.draw(win)
        #display the rounds played and high score
        roundsText = Text(Point(180, 20), "Rounds played: " + str(rounds))
        roundsText.setSize(13)
        roundsText.draw(win)
        highScoreText = Text(Point(350, 20), "Your high score: " + str(highScore))
        highScoreText.setSize(13)
        highScoreText.draw(win)
        #create five Die objects
        die1 = Die(win, Point(80, 300), 50)
        die2 = Die(win, Point(160, 300), 50)
        die3 = Die(win, Point(240, 300), 50)
        die4 = Die(win, Point(320, 300), 50)
        die5 = Die(win, Point(400, 300), 50)
        #create roll button
        rollButton = Button(win, Point(240, 400), 70, 30, "Roll")
        rollButton.setFill("light gray")

        #create a button for each score cell with the starting value of 0
        #these are buttons so that the user can click them, and there is an easy way to change
        #the label and activate/deactivate them
        oneButton = Button(win, Point(700, 100), 50, 25, "0")
        oneButton.setFill("white")
        oneText = Text(Point(650, 100), "Ones")
        oneText.draw(win)
        
        twoButton = Button(win, Point(700, 125), 50, 25, "0")
        twoButton.setFill("white")
        twoButton.activate()
        twoText = Text(Point(650, 125), "Twos")
        twoText.draw(win)
        
        threeButton = Button(win, Point(700, 150), 50, 25, "0")
        threeButton.setFill("white")
        threeButton.activate()
        threeText = Text(Point(650, 150), "Threes")
        threeText.draw(win)
        
        fourButton = Button(win, Point(700, 175), 50, 25, "0")
        fourButton.setFill("white")
        fourText = Text(Point(650, 175), "Fours")
        fourText.draw(win)
        
        fiveButton = Button(win, Point(700, 200), 50, 25, "0")
        fiveButton.setFill("white")
        fiveButton.activate()
        fiveText = Text(Point(650, 200), "Fives")
        fiveText.draw(win)
        
        sixButton = Button(win, Point(700, 225), 50, 25, "0")
        sixButton.setFill("white")
        sixText = Text(Point(650, 225), "Sixes")
        sixText.draw(win)
        
        sumButton = Button(win, Point(700, 250), 50, 25, "0")
        sumButton.setFill("light gray")
        sumText = Text(Point(650, 250), "Sum")
        sumText.setStyle("bold")
        sumText.draw(win)

        threeKindButton = Button(win, Point(700, 275), 50, 25, "0")
        threeKindButton.setFill("white")
        threeKindText = Text(Point(625, 275), "Three of a Kind")
        threeKindText.draw(win)

        fourKindButton = Button(win, Point(700, 300), 50, 25, "0")
        fourKindButton.setFill("white")
        fourKindText = Text(Point(625, 300), "Four of a Kind")
        fourKindText.draw(win)

        fullHouseButton = Button(win, Point(700, 325), 50, 25, "0")
        fullHouseButton.setFill("white")
        fullHouseText = Text(Point(635, 325), "Full House")
        fullHouseText.draw(win)

        smallStraightButton = Button(win, Point(700, 350), 50, 25, "0")
        smallStraightButton.setFill("white")
        smallStraightText = Text(Point(625, 350), "Small Straight")
        smallStraightText.draw(win)

        largeStraightButton = Button(win, Point(700, 375), 50, 25, "0")
        largeStraightButton.setFill("white")
        largeStraightText = Text(Point(625, 375), "Large Straight")
        largeStraightText.draw(win)

        chanceButton = Button(win, Point(700, 400), 50, 25, "0")
        chanceButton.setFill("white")
        chanceText = Text(Point(640, 400), "Chance")
        chanceText.draw(win)

        yahtzeeButton = Button(win, Point(700, 425), 50, 25, "0")
        yahtzeeButton.setFill("white")
        yahtzeeText = Text(Point(640, 425), "Yahtzee")
        yahtzeeText.draw(win)

        totalButton = Button(win, Point(700, 450), 50, 25, "0")
        totalButton.setFill("light gray")
        totalText = Text(Point(640, 450), "Total")
        totalText.setStyle("bold")
        totalText.draw(win)
        #activate all score cell buttons
        oneButton.activate()
        twoButton.activate()
        threeButton.activate()
        fourButton.activate()
        fiveButton.activate()
        sixButton.activate()
        threeKindButton.activate()
        fourKindButton.activate()
        fullHouseButton.activate()
        smallStraightButton.activate()
        largeStraightButton.activate()
        chanceButton.activate()
        yahtzeeButton.activate()
        #i created a variable for each cell to set whether the user has already "played" a cell
        #so that the number does not reset every time
        oneactive = True
        twoactive = True
        threeactive = True
        fouractive = True
        fiveactive = True
        sixactive = True
        threekindactive = True
        fourkindactive = True
        fullhouseactive = True
        smallstraightactive = True
        largestraightactive = True
        chanceactive = True
        yahtzeeactive = True
        #the sum is the sum of the ones, twos, threes, fours, fives, and sixes
        #it starts at zero and adds to itself as cells are played
        scoresum = 0
        #the total is the sum of all the cells, also starting at zero and adding to itself
        scoretotal = 0
        #loop for 13 times because there are 13 playable cells
        for i in range(13):
            #the variable "end" ends a turn (set of three rolls) when true, so at the beginning
            #of each turn it resets to False
            end = False
            #the variable "turn" ends a roll when False, so at the beginning of each turn it
            #resets to true
            turn = True
            #the variable "roll" determines whether the user has clicked Roll or not
            roll = False
            #rollNum counts the number of rolls in a turn to deactivate the Roll button after
            #three rolls
            rollNum = 0
            #all dice are activated at the beginning of a turn
            die1.activate()
            die2.activate()
            die3.activate()
            die4.activate()
            die5.activate()
            #setWidth to visually reset them to the "not frozen" look
            die1.setWidth(1)
            die2.setWidth(1)
            die3.setWidth(1)
            die4.setWidth(1)
            die5.setWidth(1)
            #activate roll button
            rollButton.activate()
            #set the label of the sum and total cells to be the new values
            #I am also now realizing that these cells did not need to be buttons because
            #they are never clickable but I'm going to keep them that way because it works
            sumButton.setLabel(scoresum)
            totalButton.setLabel(scoretotal)
            #while loop and if statement to start everything when the roll button is clicked
            while not roll:
                if rollButton.clicked(win.getMouse()):
                    #set roll to true to break the while loop
                    roll = True
                    #while the turn has not ended, but this while loop will only ever run three
                    #times because the roll button deactivates after three rolls, forcing you to
                    #pick a cell
                    while not end:
                        turn = True
                        #count roll number
                        rollNum += 1
                        #use die roll method to roll them all
                        die1.roll()
                        die2.roll()
                        die3.roll()
                        die4.roll()
                        die5.roll()
                        #if dice have been rolled three times, the dice and roll button
                        #deactivate and the message box tells the user to click a cell
                        if rollNum == 3:
                            rollButton.deactivate()
                            die1.deactivate()
                            die2.deactivate()
                            die3.deactivate()
                            die4.deactivate()
                            die5.deactivate()
                            messageText.setText("Click a cell to proceed.")
                        #if the dice haven't been rolled three times yet, the message is
                        #different
                        else:
                            messageText.setText("Click a score cell, click dice to freeze, "
                                                "or roll again.")
                        #using score cell class to create the score cell object using the values
                        #of the dice
                        scorecell = ScoreCell(die1.getVal(), die2.getVal(), die3.getVal(), die4.getVal(), die5.getVal())
                        #if there isn't yet a score for the ones, display the potential score
                        #of the ones, and same idea for all cells
                        #this uses the methods of score cell to get the value for the label
                        if oneactive:
                            oneButton.setLabel(scorecell.ones())
                        if twoactive:
                            twoButton.setLabel(scorecell.twos())
                        if threeactive:
                            threeButton.setLabel(scorecell.threes())
                        if fouractive:
                            fourButton.setLabel(scorecell.fours())
                        if fiveactive:
                            fiveButton.setLabel(scorecell.fives())
                        if sixactive:
                            sixButton.setLabel(scorecell.sixes())
                        if threekindactive:
                            threeKindButton.setLabel(scorecell.threekind())
                        if fourkindactive:  
                            fourKindButton.setLabel(scorecell.fourKind())
                        if fullhouseactive:
                            fullHouseButton.setLabel(scorecell.fullHouse())
                        if smallstraightactive:
                            smallStraightButton.setLabel(scorecell.smallStraight())
                        if largestraightactive:
                            largeStraightButton.setLabel(scorecell.largeStraight())
                        if chanceactive:
                            chanceButton.setLabel(scorecell.chance())
                        if yahtzeeactive:
                            yahtzeeButton.setLabel(scorecell.yahtzee())
                        #this is the code for one roll using a while loop that ends when any cell
                        #is clicked or when the dice are rerolled
                        while turn:
                            #I used click so that all of the if statements could happen with one
                            #click instead of requiring mulitiple
                            click = win.getMouse()
                            #quit button ends game and closes window
                            if quitButton.clicked(click):
                                win.close()
                                go = False
                            #clicking on a cell ends both the roll (set turn to False) and the
                            #turn (set end to True), it adds to the sum and the total, prevents
                            #the user from reclicking the cell by deactivating the button and
                            #setting [cellname]active to False, and edits the text box message
                            #to prompt the user to roll again
                            elif oneButton.clicked(click):
                                oneButton.deactivate()
                                turn = False
                                end = True
                                oneactive = False
                                scoresum += int(oneButton.getLabel())
                                scoretotal += int(oneButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif twoButton.clicked(click):
                                twoButton.deactivate()
                                turn = False
                                end = True
                                twoactive = False
                                scoresum += int(twoButton.getLabel())
                                scoretotal += int(twoButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif threeButton.clicked(click):
                                threeButton.deactivate()
                                turn = False
                                end = True
                                threeactive = False
                                scoresum += int(threeButton.getLabel())
                                scoretotal += int(threeButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif fourButton.clicked(click):
                                fourButton.deactivate()
                                turn = False
                                end = True
                                fouractive = False
                                scoresum += int(fourButton.getLabel())
                                scoretotal += int(fourButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif fiveButton.clicked(click):
                                fiveButton.deactivate()
                                turn = False
                                end = True
                                fiveactive = False
                                scoresum += int(fiveButton.getLabel())
                                scoretotal += int(fiveButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif sixButton.clicked(click):
                                sixButton.deactivate()
                                turn = False
                                end = True
                                sixactive = False
                                scoresum += int(sixButton.getLabel())
                                scoretotal += int(sixButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif threeKindButton.clicked(click):
                                threeKindButton.deactivate()
                                turn = False
                                end = True
                                threekindactive = False
                                scoretotal += int(threeKindButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif fourKindButton.clicked(click):
                                fourKindButton.deactivate()
                                turn = False
                                end = True
                                fourkindactive = False
                                scoretotal += int(fourKindButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif fullHouseButton.clicked(click):
                                fullHouseButton.deactivate()
                                turn = False
                                end = True
                                fullhouseactive = False
                                scoretotal += int(fullHouseButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif smallStraightButton.clicked(click):
                                smallStraightButton.deactivate()
                                turn = False
                                end = True
                                smallstraightactive = False
                                scoretotal += int(smallStraightButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif largeStraightButton.clicked(click):
                                largeStraightButton.deactivate()
                                turn = False
                                end = True
                                largestraightactive = False
                                scoretotal += int(largeStraightButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif chanceButton.clicked(click):
                                chanceButton.deactivate()
                                turn = False
                                end = True
                                chanceactive = False
                                scoretotal += int(chanceButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            elif yahtzeeButton.clicked(click):
                                yahtzeeButton.deactivate()
                                turn = False
                                end = True
                                yahtzeeactive = False
                                scoretotal += int(yahtzeeButton.getLabel())
                                messageText.setText("Click Roll to roll again.")
                            #if the dice are clicked, they are deactivated (to freeze them)
                            #and the border becomes thicker to visually indicate that
                            if die1.clicked(click):
                                die1.deactivate()
                                die1.setWidth(4)
                            if die2.clicked(click):
                                die2.deactivate()
                                die2.setWidth(4)
                            if die3.clicked(click):
                                die3.deactivate()
                                die3.setWidth(4)
                            if die4.clicked(click):
                                die4.deactivate()
                                die4.setWidth(4)
                            if die5.clicked(click):
                                die5.deactivate()
                                die5.setWidth(4)
                            #if the roll button is clicked again, this roll officially ends and
                            #it starts over
                            if rollButton.clicked(click):
                                turn = False
        #after 13 turns, the game is over and message box displays a game over text
        messageText.setText("Game over. Play again?")
        #to store a personal high score, it checks if the total score is higher than the
        #stored high score and edits the high score if so
        if scoretotal > highScore:
            highScore = scoretotal
        #adds one to round count
        rounds += 1
        #create and activate play again button
        playAgain = Button(win, Point(400, 500), 80, 40, "Play Again")
        playAgain.setFill("light gray")
        playAgain.activate()
        #get a click point, if the user clicks play again "go" stays true and the while loop
        #repeats, if the user clicks anything else "go" is false, the game ends, and the window
        #closes
        click1 = win.getMouse()
        if not playAgain.clicked(click1):
            win.close()
            go = False
        else:
            win.close()

main()
