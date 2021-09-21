#Conti Challenge-The Maze

import numpy as np

#initialising the a list of lists that contains the value of the penalty points and the values for the starting/ending points
def createMaze():
    maze=[]
    maze.append([0, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1])
    maze.append([1, 2, 1, 2, 2, 1, 3, 3, 2, 1, 2])
    maze.append([1, 2, 1, 1, 3, 1, 2, 1, 3, 1, 1])
    maze.append([2, 1, 2, 3, 1, 2, 1, 3, 1, 4, 2])
    maze.append([1, 3, 2, 1, 2, 1, 2, 1, 2, 1, 3])
    maze.append([1, 3, 1, 1, 1, 3, 3, 1, 3, 1, 3])
    maze.append([3, 1, 1, 2, 1, 4, 1, 2, 1, 3, 1])
    maze.append([3, 2, 3, 1, 2, 1, 3, 1, 1, 2, 1])
    maze.append([1, 1, 1, 1, 2, 1, 1, 3, 2, 1, 3])
    maze.append([1, 1, 2, 3, 1, 2, 1, 1, 1, 2, 1])
    maze.append([3, 2, 1, 1, 2, 3, 2, 1, 3, 3, 0])

    return maze

def createMaze2():
    maze=[]
    maze.append([0,3,1,1,2,3,1,2,3,2,1])
    maze.append([2,2,1,3,1,1,2,2,3,1,2])
    maze.append([3,1,1,2,3,1,1,1,1,3,1])
    maze.append([1,3,4,1,1,2,3,3,1,3,1])
    maze.append([2,1,3,2,2,1,2,1,3,1,3])
    maze.append([3,1,1,3,2,2,3,1,3,4,3])
    maze.append([2,1,3,2,2,1,3,1,2,1,3])
    maze.append([3,1,3,2,2,1,3,1,3,2,2])
    maze.append([2,1,1,3,1,2,3,1,2,1,2])
    maze.append([3,2,1,3,2,2,1,2,3,3,1])
    maze.append([2,3,1,3,1,2,1,3,2,1,0])

    return maze

def createMaze3():
    maze = []
    maze.append([0, 4, 1, 3, 2, 3, 1, 3, 1, 2, 2])
    maze.append([4, 2, 3, 2, 1, 2, 1, 2, 1, 1, 3])
    maze.append([1, 1, 2, 3, 1, 2, 1, 3, 3, 1, 2])
    maze.append([2, 1, 3, 1, 2, 3, 1, 3, 1, 3, 1])
    maze.append([2, 2, 3, 1, 2, 1, 2, 3, 1, 1, 2])
    maze.append([2, 1, 3, 1, 3, 2, 2, 3, 1, 3, 1])
    maze.append([2, 1, 3, 1, 2, 1, 1, 2, 3, 3, 3])
    maze.append([1, 2, 3, 1, 1, 1, 3, 1, 2, 1, 3])
    maze.append([3, 2, 1, 2, 3, 1, 3, 1, 3, 2, 1])
    maze.append([1, 2, 3, 1, 2, 3, 3, 2, 1, 2, 3])
    maze.append([2, 3, 1, 3, 2, 3, 3, 2, 1, 2, 0])

    return maze

def createMaze4():
    maze=[]
    maze.append([0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    maze.append([4, 1, 1, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])

    return maze

def createMaze5():
    maze=[]
    maze.append([0, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 4, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1])
    maze.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])

    return maze

#the function sums the minimum cost path for the first row
def sumCostPathRow(list1,list2):
    global tpCoords
    for index in range(1,len(list1)): #for every element in the first row
        if(list2[index]==4):  #if the element is a teleporter
            tpCoords.append([0,index]) #it's coordinates are stored
            return
        else: #else
            list1[index]=list1[index-1]+list2[index] # the minimum path cost is calculated for every other element in the row

#the function sums the minimum cost path for the column
def sumCostPathCol(list1,list2):
    global tpCoords
    for index in range(1,len(list1)): #for every element in the column
        if (list2[index][0] == 4): #if the element is a teleporter
            tpCoords.append([index,0]) #it's coordinates are stored
            return
        else: #else
            list1[index][0]=list1[index-1][0]+list2[index][0] #the minimum path cost is calculated for every other element in the column

#the function calculates the min path cost of every maze point until it reaches the first teleport point
#the function goes to every element of every list contained by minPathCost
def fillToFirstTP(list1, list2):
    for indexJ in range (1,len(list1)): #for every list in the list-variable
        for indexI in range(1,len(list1)): #for every element in the list
            if list2[indexJ][indexI] !=4: #if the value of the tile is not 4 it means its not a teleporter tile
                list1[indexJ][indexI]=list2[indexJ][indexI]+min(list1[indexJ-1][indexI],list1[indexJ][indexI-1])
            else: #if its a teleporter the coordinates are stored in a list
                tpCoords.append([indexJ,indexI])
                list1[indexJ][indexI]=1000
                return (indexJ,indexI) #the coordinates of the teleporter are returned

#the function calculates the min path cost of every maze point until it reaches the second teleport point
#the function goes to every element of every list contained by minPathCost
def fillToLastTP(x,copyOfList1, list2,tpCoords):
    for indexJ in range(0,len(copyOfList1)):
        for indexI in range(0,len(copyOfList1)):
            if copyOfList1[indexJ][indexI] == 0: #if a value hasn't previously been assigned to the tile
                if list2[indexJ][indexI]==4: #if the tile has value 4 it means it's a teleporting tile
                    tpCoords.append([indexJ, indexI]) #tile's coordinates are stored in
                    return (indexJ, indexI)
                else: #else, if it's a normal tile and it's not previously completed
                    if indexJ==0: #if the tile is in the first row
                        copyOfList1[indexJ][indexI]=list2[indexJ][indexI]+ copyOfList1[indexJ][indexI-1]
                    elif indexI==0: #if the tile is in the first column
                        copyOfList1[indexJ][indexI]=list2[indexJ][indexI]+ copyOfList1[indexJ-1][indexI-1]
                    else: #else we apply the default rule
                        copyOfList1[indexJ][indexI] = list2[indexJ][indexI] + min(copyOfList1[indexJ - 1][indexI], copyOfList1[indexJ][indexI - 1])

#the function is used to calculate the min path cost to every other points after the tp's are found
#the function goes to every element of every list contained by minPathCost except the first row and the first column of elements
def fillTheRest(list1,list2):
    for indexJ in range (0,len(list1)):
        for indexI in range(0,len(list1)):
            if list1[indexJ][indexI]==0 and list2[indexJ][indexI]!=4: #if a value hasn't been previously assigned to the tile the default rule is applied
                if indexJ == 0 and indexI == 0:
                    pass
                else:
                    if indexJ==0 :
                        list1[indexJ][indexI]=list2[indexJ][indexI]+list1[indexJ][indexI-1]
                    elif indexI==0:
                        list1[indexJ][indexI]=list2[indexJ][indexI]+list1[indexJ-1][indexI]
                    else:
                        list1[indexJ][indexI]=list2[indexJ][indexI]+min(list1[indexJ-1][indexI],list1[indexJ][indexI-1])

#the function is used to return the minimum cost path of the maze as an integer
def returnSolution(list1):
    mazeSolution = list1[10][10] #the solution will be stored in the last tile of the maze, the finish tile
    return mazeSolution

#the function is used to find the minimum cost path's value to reach the finish tile
def leastCostPath(list1, list2):
    sumCostPathRow(list1[0], list2[0]) #the first step is to calculate the minimum cost path for every element in the first row
    sumCostPathCol(list1, list2) #the second step is to calculate the minimum cost path for every element in the first column
    if len(tpCoords) == 0: #if there wasn't any value assigned to tpCoords previously it means that there are no tps in the first row or the first column
        (xFirstTp, yFirstTp)=fillToFirstTP(list1, list2) #the coordinates of the first tp are stored
    elif len(tpCoords)==1: #else, if there are
        xFirstTp = tpCoords[0][0]
        yFirstTp = tpCoords[0][1]
        list1[xFirstTp][yFirstTp] = 1000
    elif len(tpCoords)==2:
        xFirstTp=tpCoords[0][0]
        yFirstTp=tpCoords[0][1]
        xSecondTp=tpCoords[1][0]
        ySecondTp=tpCoords[1][1]
        list1[xFirstTp][yFirstTp] = 1000

    copyOfList1 = [[list1[x][y] for y in range(len(list1[0]))] for x in range(len(list1))]

    if len(tpCoords) == 1:
        (xSecondTp, ySecondTp)=fillToLastTP(xFirstTp,copyOfList1,list2,tpCoords) #the coordinates of the second tp are stored
    elif len(tpCoords)==2:
        (xSecondTp, ySecondTp)=(tpCoords[1][0],tpCoords[1][1])

    #the value of the tp's will be the minimum cost of the path to the other tp tile
    #for ex is the min cost path to the first tp is 12, when the first tp is used, the value of the 2nd teleport will be 12

    list1[xFirstTp][yFirstTp] = min(copyOfList1[xSecondTp - 1][ySecondTp], copyOfList1[xSecondTp][ySecondTp - 1])
    list1[xSecondTp][ySecondTp] = min(copyOfList1[xFirstTp - 1][yFirstTp], copyOfList1[xFirstTp][yFirstTp - 1])

    if xFirstTp == 0 :
        list1[xSecondTp][ySecondTp]=copyOfList1[xFirstTp][yFirstTp-1]
    elif yFirstTp == 0:
        list1[xSecondTp][ySecondTp]=copyOfList1[xFirstTp-1][yFirstTp]
    if xSecondTp==0:
        list1[xFirstTp][yFirstTp]=copyOfList1[xSecondTp][ySecondTp-1]
    elif ySecondTp==0:
        list1[xFirstTp][yFirstTp]=copyOfList1[xSecondTp-1][ySecondTp-1]

    fillToLastTP(xFirstTp,list1,list2,tpCoords)
    fillTheRest(list1, list2)

#the function is called to check if the path uses the a teleport tile
def checkTeleportTile(list2, indexJ, indexI):
    global tpCoords
    if list2[indexJ][indexI] == 4: #if the path uses a teleport tile
        if indexJ==tpCoords[0][0] and indexI==tpCoords[0][1]: #if the first found tp is used
            indexJ=tpCoords[1][0] #the coordinates of the path are changed to match with the second tp's coordinates
            indexI=tpCoords[1][1]
        elif indexJ==tpCoords[1][0] and indexI==tpCoords[1][1]: #else
            indexJ=tpCoords[0][0] #the coordinates of the path are changed to match with the first tp's coordinates
            indexI=tpCoords[0][1]
        return (indexJ, indexI)
    return False #if the path doesnt use a teleport tile False is returned and the path finder goes on normally

#the function is used to store the other possible paths that give the optimal solution
def remindPossiblePath(indexJ, indexI):
    global pathsCoordinates
    if [indexJ, indexI] not in pathsCoordinates:
        pathsCoordinates.append([indexJ, indexI]) #whenever a new path is found its starting point is stored in a list

#the function is used to find the previous tile of the path after calculating the value of the min cost path
def findPreviousTile(list1, list2, indexJ, indexI):
    if indexJ==0:
        return (indexJ, indexI-1)
    elif indexI==0:
        return (indexJ-1, indexI)
    else:
        if list1[indexJ-1][indexI] == list1[indexJ][indexI-1]: #if the value of the tile to the left and the one above are equal
            remindPossiblePath(indexJ, indexI - 1)  # it means there is another possible path
            return (indexJ-1, indexI)
        else: #else, if the value of the tile to the left and the one above are not equal
            if(list1[indexJ-1][indexI]<list1[indexJ][indexI-1]): #if the left one's value is lower
                return(indexJ-1, indexI) #its coordinates are returned
            else: #if the above one's value is lower
                return(indexJ, indexI-1) #its coordinates are returned

#the function is used to find the minimum cost path to the finish point
def findPaths(list1, list2, indexJ, indexI):
    pathList=[] # a list where the coordinates are stored will be initialised
    while indexJ!=0 or indexI!=0: #if the coordinates don't indicate the start point

        pathList.append([indexJ, indexI]) #append the coordinates to the list
        if checkTeleportTile(list2, indexJ, indexI): #if theres a teleport tile
            (indexJ,indexI)=checkTeleportTile(list2,indexJ,indexI) #the coordinates are changed
            pathList.append([indexJ,indexI]) #and appended
        (indexJ,indexI)=findPreviousTile(list1,list2,indexJ, indexI)
    pathList.append([indexJ, indexI])

    return pathList

#main

tpCoords=[]
pathsCoordinates=[]
mazePath=[]
theMaze=createMaze4()
minPathCost=list(np.zeros((11,11)))

leastCostPath(minPathCost, theMaze) #the value of the least cost path is calculated
optimalSolution=returnSolution(minPathCost) #the value is stored in a variable

mazePath.append(findPaths(minPathCost,theMaze,10,10)) #the first path is calculated

pathsCoordinates.reverse()

for element in pathsCoordinates:
    x,y=element[0],element[1]
    mazePath.append(findPaths(minPathCost, theMaze, x,y))



