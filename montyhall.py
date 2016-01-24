import random
doors = ["goat","goat","car"]
wins = 0
# 500 trials
for iteration in range(500):
    # randomize the doors
    random.shuffle(doors)
    # pick a random door
    randDoor = random.randint(0,2)
    # open that door (no switching)
    # if you get a car, you win
    if doors[randDoor] == "car":
        wins += 1
print "Win rate without swtiching: " + str(wins/500.0)
wins = 0
# 500 trials
for iteration in range(500):
    doors = ["goat","goat","car"]
    random.shuffle(doors)
    # pick a random door
    randDoor = random.randint(0,2)
    # determine which doors have goats
    # so a goat door can be opened
    goatDoors = []
    for i in range(len(doors)):
        # make sure not to add goat doors
        # that are the chosen door because
        # the chosen door is not revealed
        if doors[i] == "goat" and i != randDoor:
            goatDoors.append(i)
    # reveal a door that used to be a goat
    # so now the chosen door can be switched
    # to the other closed door
    doors[goatDoors[random.randint(0,len(goatDoors)-1)]] = "open"
    # switch the chosen door
    # to other closed door
    for i in range(len(doors)):
        if doors[i] != "open" and i != randDoor:
            switchDoor = i
    # open that door, if you
    # get a car, you win
    if doors[switchDoor] == "car":
        wins += 1
print "Win rate when swtiching: " + str(wins/500.0)
