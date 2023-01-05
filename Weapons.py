
import random

weapons = ["Lead Pipe", "Knife", "Pistol", "Rope", "Candlestick", "Wrench"]
rooms = ["Hall", "Study", "Lounge", "Billiard Room", "Library", "Conservatory", "Ballroom", "Kitchen", "Dining Room",
         "Basement"]


murderWeapon = random.choice(weapons)
murderWeaponFound = False

# placing the weapons in different rooms
knivePlacement = random.choice(rooms)
rooms.remove(knivePlacement)

leadPipePlacement = random.choice(rooms)
rooms.remove(leadPipePlacement)

pistolPlacement = random.choice(rooms)
rooms.remove(pistolPlacement)

wrenchPlacement = random.choice(rooms)
rooms.remove(wrenchPlacement)

candlePlacement = random.choice(rooms)
rooms.remove(candlePlacement)

ropePlacement = random.choice(rooms)
rooms.remove(ropePlacement)
