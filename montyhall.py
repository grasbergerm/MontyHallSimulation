import random
doors = ["goat","goat","car"]
wins = 0
for iteration in range(500):
    random.shuffle(doors)
    goatDoors = []
    for i in range(len(doors)):
        if doors[i] == "goat":
            goatDoors.append(i)
    randDoor = random.randint(0,2)
    if doors[randDoor] == "car":
        wins += 1
print "Win rate without swtiching: " + str(wins/500.0)
wins = 0
for iteration in range(500):
    doors = ["goat","goat","car"]
    random.shuffle(doors)
    randDoor = random.randint(0,2)
    goatDoors = []
    for i in range(len(doors)):
        if doors[i] == "goat" and i != randDoor:
            goatDoors.append(i)
    doors[goatDoors[random.randint(0,len(goatDoors)-1)]] = "open"
    for i in range(len(doors)):
        if doors[i] != "open" and i != randDoor:
            switchDoor = i
    if doors[switchDoor] == "car":
        wins += 1
print "Win rate when swtiching: " + str(wins/500.0)
