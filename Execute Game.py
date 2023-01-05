import Character
import Suspects
import Weapons
import Rooms
import otherObjects

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
        print('You are playing as Detective Inspector Stanley!')
        Character.mainCharacter = "Detective Inspector Stanley"
    elif choice == "2":
        print("You are playing as Miss Sally Percival!")
        Character.mainCharacter = "Miss Sally Percival"
    elif choice == "3":
        print("You are playing as Mr James Harrington")
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
            print("The rope was added to your inventory")
            if Weapons.murderWeapon == 'Rope':
                print("There is blood on the rope! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the rope to your inventory')

    if Weapons.knivePlacement == location:
        answer = input("There is a silver knife lying on the table, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
            print("The knife was added to your inventory")
            if Weapons.murderWeapon == 'Knife':
                print("There is blood on the knife! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the knife to your inventory')

    if Weapons.leadPipePlacement == location:
        answer = input("There is a lead pipe leaning against the wall, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
            print("The lead pipe was added to your inventory")
            if Weapons.murderWeapon == 'Lead Pipe':
                print("There is blood on the Lead Pipe! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the lead pipe to your inventory')

    if Weapons.wrenchPlacement == location:
        answer = input("There is a wrench in the cupboard, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
            print("The wrench was added to your inventory")
            if Weapons.murderWeapon == 'Wrench':
                print("There is blood on the Wrench! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the wrench to your inventory')

    if Weapons.candlePlacement == location:
        answer = input("There is a Candlestick on the table, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
            print("The Candlestick was added to your inventory")
            if Weapons.murderWeapon == 'Candlestick':
                print("There is blood on the Candlestick! You've found the murder weapon!")
                Weapons.murderWeaponFound = True
        elif answer.upper() == 'N':
            print('You did not add the Candlestick to your inventory')

    if Weapons.pistolPlacement == location:
        answer = input("There is a Pistol on the table, would you like to pick it up and inspect it? ")
        if answer.upper() == "Y":
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
                print('You just picked up a tube of lipstick')



initialise = input("Would you like to start the game? If yes, please enter y. If no, please enter n.")
if initialise.upper() == "Y":
    pickCharacter()
    while case != "solved":
        roomMovement(Rooms.currentLocation)
        murderedRoom(Rooms.currentLocation)
        findWeapons(Rooms.currentLocation)


