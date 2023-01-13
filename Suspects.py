import random

#NPCs
suspects = ["Miss Scarlett", "Colonel Mustard", "Mr Huxley", "Professor Bernstein", "Mrs. Peacock", "Mrs. Walters"]
# Different rooms
rooms = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen", "Dining Room",
         "Basement"]

#Asignes the murderer
murderer = random.choice(suspects)
murdererFound = False

# suspect to room assignment
missScarlettPlacement = random.choice(rooms)
rooms.remove(missScarlettPlacement)

colonelMustardPlacement = random.choice(rooms)
rooms.remove(colonelMustardPlacement)

mrHuxleyPlacement = random.choice(rooms)
rooms.remove(mrHuxleyPlacement)

professorBernsteinPlacement = random.choice(rooms)
rooms.remove(professorBernsteinPlacement)

mrsPeacockPlacement = random.choice(rooms)
rooms.remove(mrsPeacockPlacement)

mrsWaltersPlacement = random.choice(rooms)
rooms.remove(mrsWaltersPlacement)