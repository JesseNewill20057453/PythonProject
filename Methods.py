import random
import time
import datetime

'''
Name: Jesse Newill
Student Number: 20057453
Date: 7/10/2022
'''

# variables
currentRoom = 'Hall'
foundWeapon = False
foundMurderer = False
foundRoom = False
caseStatus = 'Unsolved'

# Declaring all the weapons, suspects, and rooms
weapons = ["Lead Pipe", "Knife", "Pistol", "Rope", "Candle Stick", "Wrench"]
suspects = ["Miss Scarlet", "Colonel Mustard", "Mr Huxley", "Professor Bernstein", "Mrs. Peacock", "Mrs. Walters"]
rooms = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen", "Dining Room",
         "Basement"]

# The selection process
murderer = random.choice(suspects)
# print(murderer)
weapon = random.choice(weapons)
# print(weapon)
room = random.choice(rooms)
# print(room)

# Create class that acts as a countdown
def countdown(h, m, s):
    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s

    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds=total_seconds)

        # Prints the time left on the timer
        print(timer, end="\r")

        # Delays the program one second
        time.sleep(1)

        # Reduces total time by one second
        total_seconds -= 1

    print("Bzzzt! The countdown is at zero seconds!")

"""
Welcome the player to the game and explain how it will work
"""

def welcome():
    # Enter your name
    playerName = input("Please enter your name: ")

    # Introduction
    print(f'Welcome Detective {playerName}! A person has gone missing! Mr Walters has been murdered!'
          f'\nIt is your to find out Where he was killed, who he was killed by, and what was he killed with...'

          f'\nYou will enter the house and make your way around it. You will be able to examine different objects, go into different rooms, and talk with the suspects')
    startGame = input(
        "If you would like to enter the house and start the game ENTER 1. If you would like to exit the game ENTER 0")

    if startGame == '0':
        print("Bye bye, Gameover")
    elif startGame == '1':
        print("Game initialising...")
        time.sleep(3)

#When selected this method starts an interview with one of the suspects
def suspectsToRoomAssigment():
    roomsToChooseFrom = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen",
                         "Dining Room", "Basement"]
    if murderer == 'Miss Scarlet':
        roomPlacement = room
        print(f'Miss Scarlet was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer != 'Miss Scarlet':
        roomPlacement = random.choice(roomsToChooseFrom)
        print(f'Miss Scarlet was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer == 'Colonel Mustard':
        roomPlacement = room
        print(f'Colonel Mustard was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer != 'Colonel Mustard':
        roomPlacement = random.choice(roomsToChooseFrom)
        print(f'Colonel Mustard was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer == 'Mr Huxley':
        roomPlacement = room
        print(f'Mr Huxley was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer != 'Mr Huxley':
        roomPlacement = random.choice(roomsToChooseFrom)
        print(f'Mr Huxley was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer == 'Professor Bernstein':
        roomPlacement = room
        print(f'Professor Bernstein was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer != 'Professor Bernstein':
        roomPlacement = random.choice(roomsToChooseFrom)
        print(f'Professor Bernstein was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer == 'Mrs. Peacock':
        roomPlacement = room
        print(f'Mrs. Peacock was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer != 'Mrs. Peacock':
        roomPlacement = random.choice(roomsToChooseFrom)
        print(f'Mrs. Peacock was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer == 'Mrs. Walters':
        roomPlacement = room
        print(f'Mrs. Walters was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)
    elif murderer != 'Mrs. Walters':
        roomPlacement = random.choice(roomsToChooseFrom)
        print(f'Mrs. Walters was in the {roomPlacement}')
        roomsToChooseFrom.remove(roomPlacement)

#This Method assigns a weapon to each room at random
def weaponsToRoomAssigment():
    roomsToChooseFrom = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen",
                         "Dining Room", "Basement"]

    knifePlacement = random.choice(roomsToChooseFrom)
    print(f'The knife is in the {knifePlacement}')
    roomsToChooseFrom.remove(knifePlacement)

    leadPipePlacement = random.choice(roomsToChooseFrom)
    print(f'The lead pipe is in the{leadPipePlacement}')
    roomsToChooseFrom.remove(roomsToChooseFrom)

    pistolPlacement = random.choice(roomsToChooseFrom)
    print(f'The lead pipe is in the{pistolPlacement}')
    roomsToChooseFrom.remove(roomsToChooseFrom)

    wrenchPlacement = random.choice(roomsToChooseFrom)
    print(f'The lead pipe is in the{wrenchPlacement}')
    roomsToChooseFrom.remove(roomsToChooseFrom)

    candlePlacement = random.choice(roomsToChooseFrom)
    print(f'The lead pipe is in the{candlePlacement}')
    roomsToChooseFrom.remove(roomsToChooseFrom)

    ropePlacement = random.choice(roomsToChooseFrom)
    print(f'The lead pipe is in the{ropePlacement}')
    roomsToChooseFrom.remove(roomsToChooseFrom)

#This Method shows the correct answers to the game
def solved(choiceToSolve):
    if choiceToSolve == "YES":
        print('You solved the case!')
        print(f'The murderer was: {murderer}')
        print(f'The weapon used was: {weapon}')
        print(f'The room Mr Walters was killed in was: {room}')
    elif choiceToSolve == "NO":
        print("Keep searching for clues!")
    else:
        print("Keep going, you'll find the killer!!")

#this method checks if there are any clues in the room
def inspectRoomForClues(searchForClues):
    if searchForClues == "YES":
        if moveToNewRoom() == room:
            print('There is blood on the floor!')
            print('You found the room that Mr. Walters was murdered in!')
            foundRoom == True
        elif moveToNewRoom() != room:
            print('There are no clues in this room! Keep searching!')

#This method moves the player to a new room
def moveToNewRoom(currentRoom):

    if currentRoom == 'Hall':
        print('If you would like to go to the lounge, turn left')
        print('If you would like to go to the study, turn Right')
        choice = input('Which way...? ')
        if choice == "LEFT":
            currentRoom = 'Lounge'
            print(currentRoom)
        elif choice == "RIGHT":
            currentRoom = 'Study'

    if currentRoom == 'Lounge':
        if choice == "RIGHT":
            currentRoom == 'Dining Room'
        elif choice == "BACK":
            currentRoom == 'Hall'

    if currentRoom == 'Dining Room':
        if choice == "FORWARDS":
            currentRoom == 'Kitchen'
        elif choice == "BACK":
            currentRoom == 'Lounge'

    if currentRoom == 'Kitchen':
        if choice == "RIGHT":
            currentRoom == 'Ballroom'
        elif choice == "BACK":
            currentRoom == 'Dining Room'

    if currentRoom == 'Ballroom':
        if choice == "FORWARDS":
            currentRoom == 'Conservatory'
        elif choice == "BACK":
            currentRoom == 'Kitchen'

    if currentRoom == 'Conservatory':
        if choice == "RIGHT":
            currentRoom == 'Billiard Room'
        elif choice == "BACK":
            currentRoom == 'Ballroom'

    if currentRoom == 'Billiard Room':
        if choice == "FORWARDS":
            currentRoom == 'Library'
        elif choice == "BACK":
            currentRoom == 'Conservatory'

    if currentRoom == 'Library':
        if choice == "FORWARDS":
            currentRoom == 'Study'
        elif choice == "BACK":
            currentRoom == 'Billiard Room'

    if currentRoom == 'Study':
        if choice == "RIGHT":
            currentRoom == 'Hall'
        elif choice == "BACK":
            currentRoom == 'Library'
    return currentRoom

#This method checks clues on different objects
def inspectObjectForClues(object):
    print(f'You have found a {object}')
    checkForClues = input('Would you like to check for any clues on the object: ')

    if checkForClues.upper() == 'YES':
        if object == weapon:
            if weapon == "Candlestick":
                print(f'There is a bloodstain on the back the {weapon}!')
                print('You found the object that Mr. Walters was murdered with!')
                foundWeapon == True
            elif weapon == "Lead Pipe":
                print(f'There is a bloodstain on the back the {weapon}!')
                print('You found the object that Mr. Walters was murdered with!')
                foundWeapon == True
            elif weapon == "Knife":
                print(f'There is a bloodstain on the blade of the {weapon}!')
                print('You found the object that Mr. Walters was murdered with!')
                foundWeapon == True
            elif weapon == "Pistol":
                print(f'There is a bullet missing from the {weapon}!')
                print('You found the object that Mr. Walters was murdered with!')
                foundWeapon == True
            elif weapon == "Rope":
                print(f'There is blood on this length of {weapon}!')
                print('You found the object that Mr. Walters was murdered with!')
                foundWeapon == True
            elif weapon == "Wrench":
                print(f'There is a bloodstain on the back the {weapon}!')
                print('You found the object that Mr. Walters was murdered with!')
                foundWeapon == True

        elif object != weapon:
            print('There are no clues on this object, keep searching!')
    elif checkForClues.upper() == 'NO':
        print("Very confident, maybe you've found the weapon already")

def runGame():
    while caseStatus != 'Solved':
        print('The case is unsolved')

suspectsToRoomAssigment()
welcome()

while caseStatus != "solved":

    moveToNewRoom(currentRoom)