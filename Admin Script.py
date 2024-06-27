# PSEC CA1 Admin Script
# 
# Student ID: p2227436
# Name: Ng Ye Kai
# Class: DISM/FT/1B/01
# Assessment: CA1-1
# 
# Scipt name: PSEC CA1 Admin Script.py
# Purpose: To manage the word pool for hangman.py as well as the game settings
# Usage syntax: Run with play button at top right
# Input files: word_list.txt, gamesettings.txt, game_log.txt
# Output files: word_list.txt, gamesettings.txt
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
import time
# reading the data from the file
with open('word_list.txt') as f:
	data = f.read()
with open('gamesettings.txt') as f:
	data2 = f.read()
with open('game_log.txt') as f:
	data3 = f.read()

# reconstructing the data as a dictionary/list
words = ast.literal_eval(data)
settings = ast.literal_eval(data2)
allplayers = ast.literal_eval(data3)

# reading game settings
attempts = int(settings["number of attempts"])
wordsagame = int(settings["number of words"])
top = int(settings["number of top players"])

password = ""
# checking password
while password != "qQ1@":
	password = input("Please input password to access script: ")
	if password != "qQ1@":
		print("Wrong password!")

# script loop start
counter = 0
while counter != 1:
	counter1 = input("What would you like to do?\n1: Edit word pool\n2: Edit game settings\n3: Print report\n4: Exit\n> ")
	# edit word pool
	if counter1 == "1":
		whattodo = 0
		while whattodo != 1:
			whattodo = input("What would you like to do?\n1: Add a word and meaning\n2: Edit a word or meaning\n3: Delete a word and meaning\n4: View Dictionary\n5: Go back\n> ")
			# adding new word and meaning
			if whattodo == "1":
				# inputting word 
				addword = input("Please input the word to be added: ")
				# checking for existing word
				if words.get(addword) == None:
					# inputting meaning
					addmeaning = input("Please input the meaning for the word: ")
					# adding to dictionary
					words[addword] = addmeaning
					# changing word_list.txt
					temp = str(words)
					f = open("word_list.txt", "w")
					f.write(temp)
					f.close()
					print("Added to word pool!")
				else:
					# prints if word already exists in dictionary
					print("Word already exists!")
			# editing existing word and meaning
			elif whattodo == "2":
				edited = input("Please input word to be edited: ")
				# checking if word exists
				if words.get(edited) == None:
					print("Word does not exist!")
				else:
					# removing old word and meaning
					words.pop(edited)
					# inputting new word and meaning
					addword = input("Please input the new word to replace it, or type the same word otherwise: ")
					addmeaning = input("Please input the new meaning for the word: ")
					# changing dictionary
					words[addword] = addmeaning
					# changing word_list.txt
					temp = str(words)
					f = open("word_list.txt", "w")
					f.write(temp)
					f.close()
					print("Added to word pool!")
			# delete existing word and meaning
			elif whattodo == "3":
				edited = input("Please input word to be deleted: ")
				# checking if word exists
				if words.get(edited) == None:
					print("Word does not exist!")
				else:
					# removing old word and meaning
					words.pop(edited)
					temp = str(words)
					f = open("word_list.txt", "w")
					f.write(temp)
					f.close()
					print("Deleted from word pool!")
			elif whattodo == "4":
				print(words)
			elif whattodo == "5":
				break
			else:
				print("Invalid input!")

	# edit game settings
	elif counter1 == "2":
		whattodo = 0
		while whattodo != "4":
			whattodo = input("What would you like to do?\n1: Edit number of attempts per word\n2: Edit number of words a game\n3: Edit amount of players shown when asking for top x player info\n4: Go back\n> ")
			# changing attempts per word
			if whattodo == "1":
				print("Current: " + str(attempts))
				changed = input("What would you like to change it to?\n> ")
				try:
					int(changed)
				except:
					print("Not a valid input!")
					break
				else:
					settings["number of attempts"] = changed
					temp = str(settings)
					f = open("gamesettings.txt", "w")
					f.write(temp)
					f.close()
					print("Settings changed!")
			# changing words per game
			elif whattodo == "2":
				print("Current: " + str(wordsagame))
				changed = input("What would you like to change it to?\n> ")
				try:
					int(changed)
				except:
					print("Not a valid input!")
					break
				else:
					settings["number of words"] = changed
					temp = str(settings)
					f = open("gamesettings.txt", "w")
					f.write(temp)
					f.close()
					print("Settings changed!")
			# changing top player count
			elif whattodo == "3":
				print("Current: " + str(top))
				changed = input("What would you like to change it to?\n> ")
				try:
					int(changed)
				except:
					print("Not a valid input!")
					break
				else:
					settings["number of top players"] = changed
					temp = str(settings)
					f = open("gamesettings.txt", "w")
					f.write(temp)
					f.close()
					print("Settings changed!")
			elif whattodo == "4":
				break
			else:
				print("Invalid input!")
	# print report
	elif counter1 == "3":
		startdate = 0
		haveenddate = False
		savedplayers = allplayers
		if "1" == input("Would you like to specify start date? Enter 1 to confirm: "):
			try:
				startdate = int(input("Please enter start date in seconds since Epoch: "))
				if startdate < 0:
					print("Input cannot be less than 0!")
					continue
			except:
				print("Invalid input!")
		if "1" == input("Would you like to specify end date? Enter 1 to confirm: "):
			try:
				enddate = int(input("Please enter end date in seconds since Epoch: "))
				if enddate < 0:
					print("Input cannot be less than 0!")
					continue
			except:
				print("Invalid input!")
			haveenddate = True
		for x in range(2,len(savedplayers),3):
			if savedplayers[x] < startdate:
				savedplayers.pop(x)
				savedplayers.pop(x-1)
				savedplayers.pop(x-2)
			elif haveenddate == True and savedplayers[x] > enddate:
				savedplayers.pop(x)
				savedplayers.pop(x-1)
				savedplayers.pop(x-2)
		print("Games played:")
		for x in range(0,len(savedplayers),3):
			print("Player name: " + savedplayers[x] + "\tPoints: " + str(savedplayers[x+1]) + "\tDate achieved: " + time.ctime(savedplayers[x+2]))

	# exit statement
	elif counter1 == "4":
		print("Thank you and goodbye!")
		break
	# invalid input statement
	else:
		print("Invalid input!")
		continue



