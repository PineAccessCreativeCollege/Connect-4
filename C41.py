from array import *
import time

completedIn = False
Grid = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]

for i in Grid:
    print(i)

inp = input("Enter a position on the grid eg.[00]")

for s in inp:
    if completedIn == True:
        pos2 = s
    else:
        pos1 = s
        completedIn = True

print(pos1, pos2)

tP1 = int(pos1)
tP2 = int(pos2)

if tP1 > 5:
    print("error: out of range 1")
if tP2 > 5:
    print("error: out of range 2")

if Grid[tP1][tP2] <= 0:
    Grid[tP1][tP2] = 1

for i in Grid:
    print(i)

nF = True

trueTimes0 = 0
trueTimes1 = 0
trueTimes2 = 0
trueTimes3 = 0

final0 = False
final1 = False
final2 = False
final3 = False

#time.sleep(5)

for i in range(3):
    i += 1

    print(i)
    
    try:
        if Grid[tP1+i][tP2+i] == 1 & final0 == False:
            print(Grid[tP1+i][tP2+i])
            trueTimes0 += 1

    except IndexError:
            final0 = True
    try:
        if Grid[tP1+i][tP2-i] == 1 & final1 == False:
            print(Grid[tP1+i][tP2-i])
            trueTimes1 += 1

    except IndexError:
            final1 = True
    try:
        if Grid[tP1-i][tP2+i] == 1 & final2 == False:
            print(Grid[tP1-i][tP2+i])
            trueTimes2 += 1

    except IndexError:
            final2 = True
    try:
        if Grid[tP1-i][tP2-i] == 1 & final3 == False:
            print(Grid[tP1-i][tP2-i])
            trueTimes3 += 1

    except IndexError:
            final3 = True

    

print(trueTimes0, trueTimes1, trueTimes2, trueTimes3)


            






#def LineChecker(placePos, Grid):
    #for 