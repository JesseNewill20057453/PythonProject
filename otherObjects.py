import random

import random
rooms = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen", "Dining Room",
         "Basement"]
roomsWithoutBasement = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen", "Dining Room"]
inventory = []

key = "Basement Key"
keyPlacement = random.choice(roomsWithoutBasement)
roomClue = "bloodstained"

# clues
clue = ""
missScarletClue = "Tube of Lipstick"
colonelMustardClue = "Monocole"
mrHuxleyClue = "Cuff link"
professorBernsteinClue = "Chalk Stick"
mrsPeacockClue = "Blue Feather"
mrsWaltersClue = "Earrring"

hasKey = False