import random
rooms = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen", "Dining Room",
         "Basement"]
roomsWithoutBasement = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen", "Dining Room"]

# inventory starts as empty
inventory = []

#special objects
key = "Basement Key"
hasKey = False

# puts the key in a room that isn't the basement
keyPlacement = random.choice(roomsWithoutBasement)
roomClue = "bloodstained"

#amount of moves
move = 15

# clues
clue = ""
case = "unsolved"
missScarletClue = "Tube of Lipstick"
colonelMustardClue = "Monocole"
mrHuxleyClue = "Cuff link"
professorBernsteinClue = "Chalk Stick"
mrsPeacockClue = "Blue Feather"
mrsWaltersClue = "Earrring"

