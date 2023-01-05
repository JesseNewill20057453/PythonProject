import random
rooms = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen", "Dining Room",
         "Basement"]

currentLocation = "Hall"
crimeScene = random.choice(rooms)
crimeSceneFound = False

hallDescription = "You have entered the hall. It is a well lit room with a table in the centre. There four doors in this room in total." \
                  "The first door is behind you, it is the one you enter and leave the house from. In front of you there are two doors to your left and right." \
                  "The door on your left leads to the lounge. The door on your right leads to the study. There is one more door in the Hall, which is directly opposite you." \
                  "It appears to be locked shut. You might need to find a key to open it. The hall may have some interesting objects in it."
hallMovement = "Options to move are: N into the basement, W into the lounge, E into the study, S to exit the game."

studyDescription = "You have entered the study"
studyMovement = "Options to move are: N into the Library, or W into the Hall"

loungeDescription = "You have entered the lounge"
loungeMovement = "Options to move are: N into the Dining Room, E into the Hall"

billiardRoomDescription = "You have entered the Billiard Room"
billiardRoomMovement ="Options to move are N into the Conservatory, or S into the Library"

libraryDescription = "You have entered the Library"
libraryMovement = "Options to move are: N into the Billiard Room, or S into the Study"

conservatoryDescription = "You have entered the Conservatory"
conservatoryMovement = "Options to move are W into the Ballroom, or S into the Billiard Room"

ballroomDescription = "You have entered the Ballroom"
ballroomMovement = "Options to move are W into the Kitchen, or E into the Conservatory"

kitchenDescription = "You have entered the Kitchen"
kitchenMovement = "Options to move are S into the Dining Room, or E into the Ballroom"

diningRoomDescription = "You have entered the Dining Room"
diningRoomMovement = "Options to move are: N into the Kitchen or S into the Lounge"

basementDescription = "You have entered the Basement"
basementMovement = "Options to move are S into the Hall"


