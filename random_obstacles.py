from config import *
import random


def create_oil_slick(locations, destination, oil_slick_chance):
    n = len(locations[0])

    for col in range(n):
        for row in range(n):
            # No slicks beneath start and end points
            if(not ((col == 0 and row == 0) or (col == destination[1] and col == destination[0]))):
                if(locations[row][col] == 0 and random.random() < oil_slick_chance):
                    locations[row][col] = 3
    return locations

def create_teleporter(locations, number_of_teleporters):
    n = len(locations[0])
    validWalls = []

    for col in range(n):
        for row in range(n):
            # No slicks beneath start and end points
                if(locations[row][col] == 1):
                    if(row > 0 and locations[row-1][col] == 0):
                        validWalls.append((row, col))
                    elif(row < n-1 and locations[row+1][col] == 0):
                        validWalls.append((row, col))
                    elif(col < n-1 and locations[row][col+1] == 0):
                        validWalls.append((row, col))  
                    elif(col > 0 and locations[row][col-1] == 0):
                        validWalls.append((row, col))                 
    numValid = len(validWalls)
    teleporterPairs = []

    index = 0
    while index < number_of_teleporters:
        teleporterPosOne = int(random.random() * (numValid - 1)) 
        teleporterPosTwo = int(random.random() * (numValid - 1))
        if(teleporterPosOne != teleporterPosTwo):
            teleporterOne = validWalls[teleporterPosOne]
            teleporterTwo = validWalls[teleporterPosTwo]
            teleporterPairs.append((teleporterOne, teleporterTwo))
            locations[teleporterOne[1]][teleporterOne[0]] = 4
            locations[teleporterTwo[1]][teleporterTwo[0]] = 4
            index += 1

    return locations, teleporterPairs