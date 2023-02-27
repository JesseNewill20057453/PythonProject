import random
rooms = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen", "Dining Room",
         "Basement"]

#Player starts in the hall
currentLocation = "Hall"

#assignes the crime scene
crimeScene = random.choice(rooms)
crimeSceneFound = False

#Descriptions of each room and options of where the player can move
hallDescription = "You are in the hall. It is a well lit room with a table in the centre. There four doors in this room in total.\n" \
                  "The first door is behind you, it is the one you enter and leave the house from. In front of you there are two doors to your left and right.\n" \
                  "The door on your left leads to the lounge. The door on your right leads to the study. There is one more door in the Hall, which is directly opposite you.\n" \
                  "It appears to be locked shut. You might need to find a key to open it. The hall may have some interesting objects in it.\n"
hallMovement = "Options to move are: N into the basement, W into the lounge, E into the study, S to exit the game. Where do you want to go? "

studyDescription = "You are in the study. There are lots of books on the shelves and a desk on the corner of the room. There are two doors in the room in total.\n" \
                   "The first door is on the west side of the room and leads to the hall. The second door is on the north side of the room and leads to the library.\n"
studyMovement = "Options to move are: N into the Library, or W into the Hall. Where do you want to go? "

loungeDescription = "You are in the lounge. It is a comfy looking room with lots of couches. There are two doors in this room.\n" \
                    "The first door is on the east side of the room and leads to the hall. The second door is on the north side of the room and leads to the dining room."
loungeMovement = "Options to move are: N into the Dining Room, E into the Hall. Where do you want to go? "

billiardRoomDescription = "You are in the Billiard Room. The room has a green billiard table in the centre. There are two doors in this room. \n" \
                          "The first door is on the north side of the room and leads to the conservatory. The second door is on the south side of the room and leads to the library."
billiardRoomMovement ="Options to move are: N into the Conservatory, or S into the Library. Where do you want to go? "

libraryDescription = "You are in the Library. All the walls are covered with bookshelves from floor to ceiling. There are two doors in this room. \n" \
                     "The first door is on the north side of the room and leads to the billiard room. The second door is on the south side of the room and leads to the study."
libraryMovement = "Options to move are: N into the Billiard Room, or S into the Study. Where do you want to go? "

conservatoryDescription = "You are in the Conservatory. Sunlight shines through the glass window that make up the room's walls. There are two doors in this room.\n" \
                          "The first door is on the west side of the room and leads to the ballroom. The second door is on the south side of the room and leads to the billiard room."
conservatoryMovement = "Options to move are: W into the Ballroom, or S into the Billiard Room. Where do you want to go? "

ballroomDescription = "You are in the Ballroom. The ballroom is the grandest room in the house. There are two doors in this room.\n" \
                      "The first door is on the west side of the room and leads to the kitchen. The second door is the east side of the room and leads to the conservatory."
ballroomMovement = "Options to move are: W into the Kitchen, or E into the Conservatory. Where do you want to go? "

kitchenDescription = "You are in the Kitchen. Fancy, modern, and completely clean in every corner. There are two doors in this room.\n" \
                     "The first door is on the south side of the room and leads to the dining room. The second door is on the east side of the room and leads to the ballroom."
kitchenMovement = "Options to move are: S into the Dining Room, or E into the Ballroom. Where do you want to go? "

diningRoomDescription = "You are in the Dining Room. Old fashioned and fancy, this room looks like it came straight out of the 1920s. There are two doors in this room.\n" \
                        "The first door is on the north side of the room and leads into the kitchen. The second door is on the south side of the room and leads to the lounge."
diningRoomMovement = "Options to move are: N into the Kitchen or S into the Lounge. Where do you want to go? "

basementDescription = "You are in the Basement. It's dark and damp and full of stuff. There is one door in this room\n" \
                      "The only door in this room is on the south side of the room "
basementMovement = "Options to move are: S into the Hall. Where do you want to go? "


