import Character
import Suspects
import Weapons
import Rooms
import otherObjects
import time
import datetime

case = "unsolved"
# location = ""
# The selection process
print(f'The murderer was {Suspects.murderer}')
print(f'The murder was commited in the {Rooms.crimeScene}')
print(f'The weapon used was a {Weapons.murderWeapon}')

def pickCharacter():
    choice = input("Choose your character: "
                   "\n1. Detective Inspector Stanley: ENTER 1 to choose..."
                   "\n2. Miss Sally Percival: ENTER 2 to choose..."
                   "\n3. Mr James Harrington: ENTER 3 to choose...")
    while choice > "4":
        choice = input("Choose your character: "
                       "\n1. Detective Inspector Stanley: ENTER 1 to choose..."
                       "\n2. Miss Sally Percival: ENTER 2 to choose..."
                       "\n3. Mr James Harrington: ENTER 3 to choose...")
    if choice == "1":
        print('\nYou are playing as Detective Inspector Stanley!')
        Character.mainCharacter = "Detective Inspector Stanley"
    elif choice == "2":
        print("\nYou are playing as Miss Sally Percival!")
        Character.mainCharacter = "Miss Sally Percival"
    elif choice == "3":
        print("\nYou are playing as Mr James Harrington")
        Character.mainCharacter = "Mr James Harrington"

def roomMovement (location):
    if location == 'Hall':
        print(Rooms.hallDescription)
        move = input(Rooms.hallMovement)
        if move.upper() == "N":
            if otherObjects.hasKey == True:
                print("You have entered the Basement")
                Rooms.currentLocation = 'Basement'
            elif otherObjects.hasKey == False:
                print("The basement door appears to be locked, it needs a key to be opened")
                Rooms.currentLocation = 'Hall'
        elif move.upper() == "W":
            print("You have chosen to enter the Lounge")
            Rooms.currentLocation = 'Lounge'
        elif move.upper() == "E":
            print("You have chosen to enter the Study")
            Rooms.currentLocation = 'Study'
        elif move.upper() == "S":
            print("You have chosen to exit the game")
            Rooms.currentLocation = ''

    if location == 'Lounge':
        print(Rooms.loungeDescription)
        move = input(Rooms.loungeMovement)
        if move.upper() == "N":
            print('You have chosen to enter the Dining Room')
            Rooms.currentLocation = 'Dining Room'
        elif move.upper() == "E":
            print("You have chosen to enter the Hall")
            Rooms.currentLocation = 'Hall'


    if location == 'Dining Room':
        print(Rooms.diningRoomDescription)
        move = input(Rooms.diningRoomMovement)
        if move.upper() == "N":
            print('You have chosen to enter the Kitchen')
            Rooms.currentLocation = 'Kitchen'
        elif move.upper() == "S":
            print('You have chosen the enter the Lounge')
            Rooms.currentLocation = 'Lounge'

    if location == 'Kitchen':
        print(Rooms.kitchenDescription)
        move = input(Rooms.kitchenMovement)
        if move.upper() == "E":
            print('You have chosen to enter the Ballroom')
            Rooms.currentLocation = 'Ballroom'
        elif move.upper() == "S":
            print('You have chosen the enter the Dining Room')
            Rooms.currentLocation = 'Dining Room'

    if location == 'Ballroom':
        print(Rooms.ballroomDescription)
        move = input(Rooms.ballroomMovement)
        if move.upper() == "W":
            print('You have chosen to enter the Kitchen')
            Rooms.currentLocation = 'Kitchen'
        elif move.upper() == "E":
            print('You have chosen the enter the Conservatory')
            Rooms.currentLocation = 'Conservatory'

    if location == 'Conservatory':
        print(Rooms.conservatoryDescription)
        move = input(Rooms.conservatoryMovement)
        if move.upper() == "W":
            print('You have chosen to enter the Ballroom')
            Rooms.currentLocation = 'Ballroom'
        elif move.upper() == "S":
            print('You have chosen the enter the Billiard Room')
            Rooms.currentLocation = 'Billiard Room'

    if location == 'Billiard Room':
        print(Rooms.billiardRoomDescription)
        move = input(Rooms.billiardRoomMovement)
        if move.upper() == "N":
            print('You have chosen to enter the Conservatory')
            Rooms.currentLocation = 'Conservatory'
        elif move.upper() == "S":
            print('You have chosen the enter the Library')
            Rooms.currentLocation = 'Library'

    if location == 'Library':
        print(Rooms.libraryDescription)
        move = input(Rooms.libraryMovement)
        if move.upper() == "N":
            print('You have chosen to enter the Billiard Room')
            Rooms.currentLocation = 'Billiard Room'
        elif move.upper() == "S":
            print('You have chosen the enter the Study')
            Rooms.currentLocation = 'Study'

    if location == 'Study':
        print(Rooms.studyDescription)
        move = input(Rooms.studyMovement)
        if move.upper() == "N":
            print('You have chosen to enter the Library')
            Rooms.currentLocation = 'Library'
        elif move.upper() == "W":
            print('You have chosen the enter the Hall')
            Rooms.currentLocation = 'Hall'

    if location == 'Basement':
        print(Rooms.basementDescription)
        move = input(Rooms.basementMovement)
        if move.upper() == "S":
            print('You have chosen to enter the Hall')
            Rooms.currentLocation = 'Hall'

def findWeapons(location):
    if Weapons.ropePlacement == location:
        answer = input("A rope is hanging from a hook on the wall, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
            otherObjects.inventory.append("Rope")
            # print(otherObjects.inventory)
            print("The rope was added to your inventory")
            if Weapons.murderWeapon == 'Rope':
                print("There is blood on the rope! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the rope to your inventory')

    if Weapons.knivePlacement == location:
        answer = input("There is a silver knife lying on the table, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
            otherObjects.inventory.append("Knife")
            # print(otherObjects.inventory)
            print("The knife was added to your inventory")
            if Weapons.murderWeapon == 'Knife':
                print("There is blood on the knife! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the knife to your inventory')

    if Weapons.leadPipePlacement == location:
        answer = input("There is a lead pipe leaning against the wall, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
            otherObjects.inventory.append("Lead Pipe")
            # print(otherObjects.inventory)
            print("The lead pipe was added to your inventory")
            if Weapons.murderWeapon == 'Lead Pipe':
                print("There is blood on the Lead Pipe! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the lead pipe to your inventory')

    if Weapons.wrenchPlacement == location:
        answer = input("There is a wrench in the cupboard, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
            otherObjects.inventory.append("Wrench")
            # print(otherObjects.inventory)
            print("The wrench was added to your inventory")
            if Weapons.murderWeapon == 'Wrench':
                print("There is blood on the Wrench! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the wrench to your inventory')

    if Weapons.candlePlacement == location:
        answer = input("There is a Candlestick on the table, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
            otherObjects.inventory.append("Candlestick")
            # print(otherObjects.inventory)
            print("The Candlestick was added to your inventory")
            if Weapons.murderWeapon == 'Candlestick':
                print("There is blood on the Candlestick! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the Candlestick to your inventory')

    if Weapons.pistolPlacement == location:
        answer = input("There is a Pistol on the table, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
            otherObjects.inventory.append("Pistol")
            # print(otherObjects.inventory)
            print("The Pistol was added to your inventory")
            if Weapons.murderWeapon == 'Pistol':
                print("There is blood on the Pistol! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the Pistol to your inventory')

def evidence(murderer):
    if murderer == "Miss Scarlet":
        otherObjects.clue = otherObjects.missScarletClue
    elif murderer == "Colonel Mustard":
        otherObjects.clue = otherObjects.colonelMustardClue
    elif murderer == "Mr Huxley":
        otherObjects.clue = otherObjects.mrHuxleyClue
    elif murderer == "Professor Bernstein":
        otherObjects.clue = otherObjects.professorBernsteinClue
    elif murderer == "Mrs. Peacock":
        otherObjects.clue = otherObjects.mrsPeacockClue
    elif murderer == "Mrs. Walters":
        otherObjects.clue = otherObjects.mrsWaltersClue

def murderedRoom(location):
    if location == 'Hall':
        if 'Hall' == Rooms.crimeScene:
            answer = input("There appears to be a stain on the floor, would you like to investigate it? ")
            if answer.upper() == 'Y':
                print(f"It's a {otherObjects.roomClue}, you must have found the room that Mr. Walters was killed in!")
                print("You've taken a photo for evidence")
                otherObjects.inventory.append("Crime Scene Photo")
                print("The photo of the crime scene was added to your inventory")
                Rooms.crimeSceneFound = True
            elif answer.upper() == 'N':
                print("It's probably just some spilt wine.")
        elif 'Hall' != Rooms.crimeScene:
            print("There doesn't appear to be any sign of murder in here.")

    elif location == 'Study':
        if 'Study' == Rooms.crimeScene:
            answer = input("There appears to be a stain on the floor, would you like to investigate it? ")
            if answer.upper() == 'Y':
                print(f"It's a {otherObjects.roomClue}, you must have found the room that Mr. Walters was killed in!")
                print("You've taken a photo for evidence")
                otherObjects.inventory.append("Crime Scene Photo")
                print("The photo of the crime scene was added to your inventory")
                Rooms.crimeSceneFound = True
            elif answer.upper() == 'N':
                print("It's probably just some spilt wine.")
        elif 'Study' != Rooms.crimeScene:
            print("There doesn't appear to be any sign of murder in here.")

    elif location == 'Lounge':
        if 'Lounge' == Rooms.crimeScene:
            answer = input("There appears to be a stain on the floor, would you like to investigate it? ")
            if answer.upper() == 'Y':
                print(f"It's a {otherObjects.roomClue}, you must have found the room that Mr. Walters was killed in!")
                print("You've taken a photo for evidence")
                otherObjects.inventory.append("Crime Scene Photo")
                print("The photo of the crime scene was added to your inventory")
                Rooms.crimeSceneFound = True
            elif answer.upper() == 'N':
                print("It's probably just some spilt wine.")
        elif 'Lounge' != Rooms.crimeScene:
            print("There doesn't appear to be any sign of murder in here.")

    elif location == 'Billiard Room':
        if 'Billiard Room' == Rooms.crimeScene:
            answer = input("There appears to be a stain on the floor, would you like to investigate it? ")
            if answer.upper() == 'Y':
                print(f"It's a {otherObjects.roomClue}, you must have found the room that Mr. Walters was killed in!")
                print("You've taken a photo for evidence")
                otherObjects.inventory.append("Crime Scene Photo")
                print("The photo of the crime scene was added to your inventory")
                Rooms.crimeSceneFound = True
            elif answer.upper() == 'N':
                print("It's probably just some spilt wine.")
        elif 'Billiard Room' != Rooms.crimeScene:
            print("There doesn't appear to be any sign of murder in here.")

    elif location == 'Library':
        if 'Library' == Rooms.crimeScene:
            answer = input("There appears to be a stain on the floor, would you like to investigate it? ")
            if answer.upper() == 'Y':
                print(f"It's a {otherObjects.roomClue}, you must have found the room that Mr. Walters was killed in!")
                print("You've taken a photo for evidence")
                otherObjects.inventory.append("Crime Scene Photo")
                print("The photo of the crime scene was added to your inventory")
                Rooms.crimeSceneFound = True
            elif answer.upper() == 'N':
                print("It's probably just some spilt wine.")
        elif 'Library' != Rooms.crimeScene:
            print("There doesn't appear to be any sign of murder in here.")

    elif location == 'Conservatory':
        if 'Conservatory' == Rooms.crimeScene:
            answer = input("There appears to be a stain on the floor, would you like to investigate it? ")
            if answer.upper() == 'Y':
                print(f"It's a {otherObjects.roomClue}, you must have found the room that Mr. Walters was killed in!")
                print("You've taken a photo for evidence")
                otherObjects.inventory.append("Crime Scene Photo")
                print("The photo of the crime scene was added to your inventory")
                Rooms.crimeSceneFound = True
            elif answer.upper() == 'N':
                print("It's probably just some spilt wine.")
        elif 'Conservatory' != Rooms.crimeScene:
            print("There doesn't appear to be any sign of murder in here.")

    elif location == 'Ballroom':
        if 'Ballroom' == Rooms.crimeScene:
            answer = input("There appears to be a stain on the floor, would you like to investigate it? ")
            if answer.upper() == 'Y':
                print(f"It's a {otherObjects.roomClue}, you must have found the room that Mr. Walters was killed in!")
                print("You've taken a photo for evidence")
                otherObjects.inventory.append("Crime Scene Photo")
                print("The photo of the crime scene was added to your inventory")
                Rooms.crimeSceneFound = True
            elif answer.upper() == 'N':
                print("It's probably just some spilt wine.")
        elif 'Ballroom' != Rooms.crimeScene:
            print("There doesn't appear to be any sign of murder in here.")

    elif location == 'Kitchen':
        if 'Kitchen' == Rooms.crimeScene:
            answer = input("There appears to be a stain on the floor, would you like to investigate it? ")
            if answer.upper() == 'Y':
                print(f"It's a {otherObjects.roomClue}, you must have found the room that Mr. Walters was killed in!")
                print("You've taken a photo for evidence")
                otherObjects.inventory.append("Crime Scene Photo")
                print("The photo of the crime scene was added to your inventory")
                Rooms.crimeSceneFound = True
            elif answer.upper() == 'N':
                print("It's probably just some spilt wine.")
        elif 'Kitchen' != Rooms.crimeScene:
            print("There doesn't appear to be any sign of murder in here.")

    elif location == 'Dining Room':
        if 'Dining Room' == Rooms.crimeScene:
            answer = input("There appears to be a stain on the floor, would you like to investigate it? ")
            if answer.upper() == 'Y':
                print(f"It's a {otherObjects.roomClue}, you must have found the room that Mr. Walters was killed in!")
                print("You've taken a photo for evidence")
                otherObjects.inventory.append("Crime Scene Photo")
                print("The photo of the crime scene was added to your inventory")
                Rooms.crimeSceneFound = True
            elif answer.upper() == 'N':
                print("It's probably just some spilt wine.")
        elif 'Dining Room' != Rooms.crimeScene:
            print("There doesn't appear to be any sign of murder in here.")

    elif location == 'Basement':
        if 'Basement' == Rooms.crimeScene:
            answer = input("There appears to be a stain on the floor, would you like to investigate it? ")
            if answer.upper() == 'Y':
                print(f"It's a {otherObjects.roomClue}, you must have found the room that Mr. Walters was killed in!")
                print("You've taken a photo for evidence")
                otherObjects.inventory.append("Crime Scene Photo")
                print("The photo of the crime scene was added to your inventory")
                Rooms.crimeSceneFound = True
            elif answer.upper() == 'N':
                print("It's probably just some spilt wine.")
        elif 'Basement' != Rooms.crimeScene:
            print("There doesn't appear to be any sign of murder in here.")

def findingClues(location):
    if location == Rooms.crimeScene:
        if Suspects.murderer == "Miss Scarlet":
            answer = input("There is something in the corner of this room, would you like to investigate it")
            if answer.upper() == 'Y':
                print(f'You just picked up a {otherObjects.missScarletClue}')
                print("This belongs to Miss Scarlett, you must have found the murderer")
                otherObjects.inventory.append(otherObjects.missScarletClue)
                print("The object was added to your inventory")
            if answer.upper() == 'N':
                print("It's probably nothing, time to keep searching...")

        elif Suspects.murderer == "Colonel Mustard":
            answer = input("There is something in the corner of this room, would you like to investigate it")
            if answer.upper() == 'Y':
                print(f'You just picked up a {otherObjects.colonelMustardClue}')
                print("This belongs to Colonel Mustard, you must have found the murderer")
                otherObjects.inventory.append(otherObjects.colonelMustardClue)
                print("The object was added to your inventory")
            if answer.upper() == 'N':
                print("It's probably nothing, time to keep searching...")

        elif Suspects.murderer == "Mr Huxley":
            answer = input("There is something in the corner of this room, would you like to investigate it")
            if answer.upper() == 'Y':
                print(f'You just picked up a {otherObjects.mrHuxleyClue}')
                print("This belongs to Mr Huxley, you must have found the murderer")
                otherObjects.inventory.append(otherObjects.mrHuxleyClue)
                print("The object was added to your inventory")
            if answer.upper() == 'N':
                print("It's probably nothing, time to keep searching...")

        elif Suspects.murderer == "Professor Bernstein":
            answer = input("There is something in the corner of this room, would you like to investigate it")
            if answer.upper() == 'Y':
                print(f'You just picked up a {otherObjects.professorBernsteinClue}')
                print("This belongs to Professor Bernstein, you must have found the murderer")
                otherObjects.inventory.append(otherObjects.professorBernsteinClue)
                print("The object was added to your inventory")
            if answer.upper() == 'N':
                print("It's probably nothing, time to keep searching...")

        elif Suspects.murderer == "Mrs. Peacock":
            answer = input("There is something in the corner of this room, would you like to investigate it")
            if answer.upper() == 'Y':
                print(f'You just picked up a {otherObjects.mrsPeacockClue}')
                print("This belongs to Mrs. Peacock, you must have found the murderer")
                otherObjects.inventory.append(otherObjects.mrsPeacockClue)
                print("The object was added to your inventory")
            if answer.upper() == 'N':
                print("It's probably nothing, time to keep searching...")

        elif Suspects.murderer == "Mrs. Walters":
            answer = input("There is something in the corner of this room, would you like to investigate it")
            if answer.upper() == 'Y':
                print(f'You just picked up a {otherObjects.mrsWaltersClue}')
                print("This belongs to Mrs. Walters, you must have found the murderer")
                otherObjects.inventory.append(otherObjects.mrsWaltersClue)
                print("The object was added to your inventory")
            if answer.upper() == 'N':
                print("It's probably nothing, time to keep searching...")

def findKey(location):
    if location == otherObjects.keyPlacement:
        choice = input('There appears to be something gold lying on the floor, would you like to inspect it? ')

        if choice.upper() == "Y":
            print("You found the key to the basement")
            otherObjects.hasKey = True
            otherObjects.inventory.append("Basement Key")
            print("The key was added to your inventory.")
        elif choice.upper() == "N":
            print("It's probably not important...")

def interview():
    choice = input("Would you like to interview someone? ")
    if choice.upper() == 'Y':
        interviewee = input("You can interview:"
                            "\n1. Miss Scarlett - ENTER 1 to interview"
                            "\n2. Colonel Mustard - ENTER 2 to interview"
                            "\n3. Mr Huxley - ENTER 3 to interview"
                            "\n4. Professor Bernstein - ENTER 4 to interview"
                            "\n5. Mrs. Peacock - ENTER 5 to interview"
                            "\n6. Mrs. Walters - ENTER 6 to interview ")
        if interviewee == "1":
            print("You are now interviewing Miss Scarlett: ")
            time.sleep(1)
            print(f'\n{Character.mainCharacter} - What room were you in at the time of the murder? ')
            if Suspects.murderer == "Miss Scarlett":
                print(f'Miss Scarlett - I was in the {Rooms.crimeScene}')
            elif Suspects.murderer != "Miss Scarlett":
                print(f'Miss Scarlett - I was in the {Suspects.missScarlettPlacement}')

        elif interviewee == "2":
            print("You are now interviewing Colonel Mustard: ")
            time.sleep(1)
            print(f'\n{Character.mainCharacter} - What room were you in at the time of the murder? ')
            if Suspects.murderer == "Colonel Mustard":
                print(f'Colonel Mustard - I was in the {Rooms.crimeScene}')
            elif Suspects.murderer != "Colonel Mustard":
                print(f'Colonel Mustard - I was in the {Suspects.colonelMustardPlacement}')

        elif interviewee == "3":
            print("You are now interviewing Mr Huxley: ")
            time.sleep(1)
            print(f'\n{Character.mainCharacter} - What room were you in at the time of the murder? ')
            if Suspects.murderer == "Mr Huxley":
                print(f'Mr Huxley - I was in the {Rooms.crimeScene} ')
            elif Suspects.murderer != "Mr Huxley":
                print(f'Mr Huxley - I was in the {Suspects.mrHuxleyPlacement} ')

        elif interviewee == "4":
            print("You are now interviewing Professor Bernstein: ")
            time.sleep(1)
            print(f'\n{Character.mainCharacter} - What room were you in at the time of the murder? ')
            if Suspects.murderer == "Professor Bernstein":
                print(f'Professor Bernstein - I was in the {Rooms.crimeScene}')
            elif Suspects.murderer != "Professor Bernstein":
                print(f'Professor Bernstein - I was in the {Suspects.professorBernsteinPlacement}')

        elif interviewee == "5":
            print("You are now interviewing Mrs. Peacock: ")
            time.sleep(1)
            print(f'\n{Character.mainCharacter} - What room were you in at the time of the murder? ')
            if Suspects.murderer == "Mrs. Peacock":
                print(f'Mrs. Peacock - I was in the {Rooms.crimeScene}')
            elif Suspects.murderer != "Mrs. Peacock":
                print(f'Mrs. Peacock - I was in the {Suspects.mrsPeacockPlacement}')

        elif interviewee == "6":
            print("You are now interviewing Mrs. Walters: ")
            time.sleep(1)
            print(f'\n{Character.mainCharacter} - What room were you in at the time of the murder? ')
            if Suspects.murderer == "Mrs. Walters":
                print(f'Mrs. Walters - I was in the {Rooms.crimeScene}')
            elif Suspects.murderer != "Mrs. Walters":
                print(f'Mrs. Walters - I was in the {Suspects.mrsWaltersPlacement}')

    elif choice.upper() == "N":
        print("You have chosen not to interview anyone...")

initialise = input("Would you like to start the game? If yes, please enter y. If no, please enter n.")
if initialise.upper() == "Y":
    pickCharacter()
    while case != "solved":
        roomMovement(Rooms.currentLocation)
        murderedRoom(Rooms.currentLocation)
        findWeapons(Rooms.currentLocation)
        findKey(Rooms.currentLocation)
        interview()


