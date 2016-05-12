running = True
currentRoom = 1
username = input("Enter name : ")
#-------------------------------------------------------
def showStatus():
    print("---------------------------")
    print(username, ("you are in the " + rooms[currentRoom]["name"]))
    print("---------------------------")
#-------------------------------------------------------
def showInstructions():
    print('''
RPG Game
========
Instructions:
    Escape the Black Plague
    You're on your own
========
Commands:
  go [direction]
  get [item]
  quit = exit
''')

username
print("Hello:")
print(username)
print('''The whole town is gripped by the Plague
You seem to be safe..for now.
''')
showInstructions()
rooms = {
    
    1: { "name" : "Your Home",
         "south" : 2,
         "east" : 3,
         
         },
    2: { "name" : "South town",
         "north" : 1,
         "south" : 5,
         },
    3: { "name" : "East town",
         "west" : 1,
         "east" : 4
         },
    4: { "name" : "Church",
         "south" : 3,
         "east" : 5,
         },
    5: { "name" : "Incinerators",
         "south" : 2,
         "west" : 6,
         },
    6: { "name" : "flagellants",
         "east" : 5,
         "west" : 7,
         },
    7: { "name" : "docks",
         "east" : 6,
         },
    8: {"name" : "Britain"
        },
    9: {"name" : "Dead Animals"
        },
    }

while True:

    showStatus()

    move = input(">").lower().split()

    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")

    if rooms[currentRoom]["name"] == "South town":
        print('''The town is full of the sick, and the sewers are full of the disease The church advises the people to not bath and sit in the sewers to protect themselves. Some advice that was...''')
        
    if rooms[currentRoom]["name"] == "East town":
        print('''The town is full of the sick, and the sewers are full of the disease. The church advises the people to not bath and sit in the sewers to protect themselve. Some advice that was...''')

    if rooms[currentRoom]["name"] == "Church":
        print('''At the church you see people praying. In this time, the people were still very religious. After the plague departed however, people lost faith in Christianityfor they didn't get protection from the plague''')

    if rooms[currentRoom]["name"] == "Incinerators":
        print("Instead of burying bodies, dead victims are burned to prevent the plague spreading")

    if rooms[currentRoom]["name"] == "flagellants":
        print('''You see people whipping themselves in the square. They are flagellants, they believe if they suffer god will spare the people''')

    if rooms[currentRoom]["name"] == "docks":
        print("Its the docks, this is your way out!(go west)")

    if rooms[currentRoom]["name"] == "Britain":
        print('''You hitched a ride the country. You thought you were uninfected, but you become sick. You die in weeks, and within days, most of the town is infected. You have doomed them all.''')

    if rooms[currentRoom]["name"] == "Dead Animals":
        print("Believing that cats and dogs were the bringers of the disease, the people slaughter them, however, this ")
