import random

weapons = ["Lead Pipe", "Knife", "Pistol", "Rope", "Candlestick", "Wrench"]
rooms = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen", "Dining Room",
         "Basement"]

# assigns the murder weapon
murderWeapon = random.choice(weapons)
murderWeaponFound = False

# placing the weapons in different rooms
knivePlacement = random.choice(rooms)
rooms.remove(knivePlacement)
knifeFound = False

leadPipePlacement = random.choice(rooms)
rooms.remove(leadPipePlacement)
leadPipeFound = False

pistolPlacement = random.choice(rooms)
rooms.remove(pistolPlacement)
pistolFound = False

wrenchPlacement = random.choice(rooms)
rooms.remove(wrenchPlacement)
wrenchFound = False

candlePlacement = random.choice(rooms)
rooms.remove(candlePlacement)
candlestickFound = False

ropePlacement = random.choice(rooms)
rooms.remove(ropePlacement)
ropeFound = False
