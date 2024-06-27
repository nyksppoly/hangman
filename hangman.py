# PSEC CA1 Hangman Script 
# 
# Student ID: p2227436
# Name: Ng Ye Kai
# Class: DISM/FT/1B/01
# Assessment: CA1-1
# 
# Scipt name: hangman.py
# Purpose: To run the hangman game and record game results
# Usage syntax: Run with play button at top right
# Input files: word_list.txt, gamesettings.txt
# Output files: game_log.txt
# Python ver: Python 3
# References:
#   https://www.geeksforgeeks.org/how-to-read-dictionary-from-file-in-python/
#   https://www.manythings.org/hmjs/voa-assorted.html
# Library/Module: None 
# Known issues: None
# 
# 
# importing the modules
import ast
import random
import time
import re
import copy
# reading the data from the file
with open('word_list.txt') as f:
	data = f.read()
with open('gamesettings.txt') as f:
	data2 = f.read()
with open('game_log.txt') as f:
	data3 = f.read()

# reconstructing the data as a dictionary
words = ast.literal_eval(data)
settings = ast.literal_eval(data2)
allplayers = ast.literal_eval(data3)

# reading game settings
attempts = int(settings["number of attempts"])
wordsagame = int(settings["number of words"])
top = int(settings["number of top players"])

# script start
counter0 = 0
while counter0 != 1:
    counter1 = input("What would you like to do?\n1: Play Hangman\n2: View top " + str(top) + " players\n3: Exit script\n>  ")

# hangman game code
    if counter1 == "1":
        # setting and verifying player name and points
        temp = 0
        while temp < 1:
            playername = input("Please input your name: ")
            checkedname = re.findall("[^a-zA-Z-/]", playername)
            if checkedname:
                print("Invalid input! Only the following characters are allowed - upper and lowercase letters, '-', and '/'")
            elif playername == "":
                print("Empty name!")
            else:
                temp = 1
        # setting lifelines and points
        lifelines = 2
        points = 0
        # checking categories
        loopcount = 0
        while loopcount < 3:
            if loopcount == 0:
                complexwords = input("Would you like to include complex words into your game? Complex words are defined as those with 10 or more characters such as strawberries, friendships, and motivation. Enter 1 if yes and 0 if no\n> ")
                if complexwords == "1" or complexwords == "0":
                    loopcount += 1
                else:
                    print("Invalid input!")
            elif loopcount == 1:
                simpleip = input("Would you like to include simple idioms-proverbs into your game?  eg., 'still waters run deep'. Enter 1 if yes and 0 if no\n> ")
                if simpleip == "1" or simpleip == "0":
                    loopcount += 1
                else:
                    print("Invalid input!")
            elif loopcount == 2:
                complexip = input("Would you like to include complex idioms-proverbs into your game? eg., 'you can lead a horse to water but you can't make it drink'. They are usually 8 or more words. Enter 1 if yes and 0 if no\n> ")
                if complexip == "1" or complexip == "0":
                    loopcount += 1
                else:
                    print("Invalid input!")
        # checking for words to remove from pool and adding them to a list
        popwords = []
        tempwords = copy.deepcopy(words)
        if complexwords == "0":
            for counting in tempwords:
                if len(counting) > 9:
                    popwords.append(counting)
        if simpleip == "0":
            for counting in tempwords:
                if len(re.findall("[ ]", counting)) > 1 and len(re.findall("[ ]", counting)) < 8:
                    popwords.append(counting)
        if complexip == "0":
            for counting in tempwords:
                if len(re.findall("[ ]", counting)) >= 8:
                    popwords.append(counting)
        # removing words from pool
        if len(popwords) > 0:
            print("Removed: " + str(popwords))
            for popnum in range(len(popwords)):
                tempwords.pop(popwords[popnum])
        # starting game loop
        for currentattempt in range(wordsagame):

            # clearing data from previous game (if any)
            correctguess = []
            wrongguess = []
            counter4 = []
            counter5 = 0
            matchvar = 0
            # picking word and meaning for the current game and removing it from pool
            word, meaning = random.choice(list(tempwords.items()))
            tempwords.pop(word)
            tempwordlist =[i for a,i in enumerate(word)]
            lifelineuse = 0
            print(word,meaning) # remove "#"" to get word + meaning in game (this is cheating)
            for counter2 in tempwordlist:
                if counter2 != " ":
                    correctguess.append("_")
                else:
                    correctguess.append(" ")
                    counter5 += 1
            if lifelines > 0:
                print("If you would like to use 1 of your lifelines to show all vowels or the meaning of the word you are guessing please type 'lifeline'. Please note that 4 points will be deducted for each lifeline used, and you can only use a lifeline once per word")
            print("Lifelines left: " + str(lifelines))
            # starting word guess loop
            counter = 0
            while counter < attempts:

                # turning objects into strings for printing
                lifeleft = attempts  - len(wrongguess)
                templife = str(lifeleft)
                tempguess = ' '.join(map(str,wrongguess))

                # checking if all words have been guessed
                if counter5 == len(tempwordlist):
                    print("You guessed the word correctly!\nAttempt: " + str(currentattempt + 1) + "\nLives left: " + templife)
                    print("Word was: " + word + "\nMeaning: " + meaning)
                    if currentattempt + 1 != wordsagame:
                        input("Next game: Press enter to start")
                    break

                print("H A N G M A N\nAttempt: " + str(currentattempt + 1) + "\nPlayer: " + playername + "\nLives left: " + templife + "\nIncorrect letters: " + tempguess)
                print("LETTERS: " + str(correctguess))

                # getting input guess
                guess = input("Select a valid character [a-z,']: ")
                guess = guess.lower()
                # checking for lifelines used
                if guess == "lifeline" and lifelineuse == 0 and lifelines > 0:
                    lifelineuse = input("Press 1 to show all vowels. Press 2 to show the meaning of the word. Press 3 to cancel lifeline usage.\n> ")
                    if lifelineuse == "1":
                        print("Showing all vowels.")
                        vowels = ["a","e","i","o","u"]
                        for vowel in vowels:
                            for counter3 in range(len(tempwordlist)):
                                if tempwordlist[counter3] == vowel:
                                    counter4.append(counter3)
                            for x in range(len(counter4)):
                                correctguess[counter4[x]] = vowel
                                counter5 += 1
                            counter4.clear()
                        counter -= 1
                        points -= 4
                        lifelines -= 1
                    elif lifelineuse == "2":
                        print("Meaning of the word is: " + meaning)
                        points -= 4
                        lifelines -= 1
                    elif lifelineuse == "3":
                        print("Canceled.")
                        continue
                    else:
                        print("Invalid input! Lifeline usage canceled.")
                # validating guess
                elif guess == "lifeline" and lifelines > 0:
                    print("You have already used your lifeline for this word!")
                    continue
                elif guess == "lifeline":
                    print("No more lifelines left!")
                    continue
                elif len(guess) > 1 or len (guess) == 0:
                    print("Invalid guess length! Only one character allowed")
                    continue
                elif guess.isnumeric() == True:
                    print("No numbers allowed! Try again")
                    continue
                elif guess == "'":
                    guess = guess
                elif guess.isalpha() == True:
                    guess = guess
                else:
                    print("Invalid guess! Try again")
                    continue

                # checking if guess is correct
                for counter3 in range(len(tempwordlist)):
                    if tempwordlist[counter3] == guess:
                        matchvar = 1
                        counter4.append(counter3)
                    elif wrongguess.count(guess) > 0:
                        print("That is an already guessed incorrect letter!")
                        matchvar = 2
                        break
                # depending on result guess is processed
                match matchvar:
                    case 1:  
                        for x in range(len(counter4)):
                            if guess == correctguess[counter4[x]]:
                                print("You have guessed that already!")
                                break
                            correctguess[counter4[x]] = guess
                            counter5 += 1
                            points += 2
                        counter -= 1
                        counter4.clear()
                        matchvar = 0
                    case 2:
                        matchvar = 0
                        counter -= 1
                    case _:
                        wrongguess.append(guess)
                # checking for remaining lives/attempts
                if counter + 1 == attempts and currentattempt + 1 == wordsagame:
                    print("You ran out of lives and attempts!")
                    print("Word was: " + word + "\nMeaning was: " + meaning)
                elif counter + 1 == attempts:
                    print("You ran out of lives! Press enter to play again")
                    input("Word was: " + word + "\nMeaning was: " + meaning)
                counter += 1
        # checking points for win/loss message
        if points > 30 and wordsagame == 3:
            points = 30
        if points > 15:
            print("You got more than 15 points! You win!")
        else:
            print("You didn't get more than 15 points. You lost.")
        # adding record to current script data
        allplayers.append(playername)
        allplayers.append(points)
        allplayers.append(time.time())
        # turning current script data into saved data
        savedplayers = allplayers.copy()
        for x in range(0,len(savedplayers),3):
            print(savedplayers[x])
            savedplayers[x] = "\"" + str(savedplayers[x]) + "\""
            print(savedplayers[x])
        written = "["
        written += ','.join(map(str, savedplayers))
        written += "]"
        f = open("game_log.txt", "w")
        f.write(written)
        f.close()

# reading and printing top players
    elif counter1 == "2":
        if len(allplayers)/3 < top:
            print("Saved data has less than " + str(top) + " records.\nDisplaying all: " + str(allplayers))
        else:
            # getting top players
            topplayers = sorted(range(1,len(allplayers),3), key = lambda sub: allplayers[sub])[-top:]
            print("Top " + str(top) + " player data: ")
            for abc in range(0,len(topplayers)):
                # printing top player info
                print("Name: " + str(allplayers[topplayers[abc]-1]) + "\t\tPoints: " + str(allplayers[topplayers[abc]]))


# exit loop statement
    elif counter1 == "3":
        print("Thank you and goodbye!")
        break

# invalid input statement
    else:
        print("Invalid input!")
        continue