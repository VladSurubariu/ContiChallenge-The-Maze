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

#the function sums the minimum cost path for the first row
def sumCostPathRow(list1,list2):
    for index in range(1,len(list1)):
        list1[index]=list1[index-1]+list2[index]

#the function sums the minimum cost path for the column
def sumCostPathCol(list1,list2):
    for index in range(1,len(list1)):
        list1[index][0]=list1[index-1][0]+list2[index][0]

#the function calculates the min path cost of every maze point until it reaches the first teleport point
#the function goes to every column in every row of the lists
def fillToFirstTP(list1, list2):
    for indexJ in range (1,len(list1)):
        for indexI in range(1,len(list1)):
            if list2[indexJ][indexI] !=4: #if the value of the tile is not 4 it means its not a teleporter tile
                list1[indexJ][indexI]=list2[indexJ][indexI]+min(list1[indexJ-1][indexI],list1[indexJ][indexI-1])
            else: #if its a teleporter the coordinates are stored in a list
                tpCoords.append([indexJ,indexI])
                print(indexJ, indexI)
                list1[indexJ][indexI]=1000
                return (indexJ,indexI) #the coordinates of the teleporter are returned

#the function calculates the min path cost of every maze point until it reaches the second teleport point
#the function goes to every row in every column of the lists
def fillToLastTP(x,list1, list2,tpCoords):
    for indexJ in range(x,len(list1)):
        for indexI in range(1,len(list1)):
            if list1[indexJ][indexI] == 0:
                if list2[indexJ][indexI]==4:
                    tpCoords.append([indexJ, indexI])
                    print(indexJ, indexI)
                    return (indexJ, indexI)
                else:
                    list1[indexJ][indexI] = list2[indexJ][indexI] + min(list1[indexJ - 1][indexI], list1[indexJ][indexI - 1])


#the function is used to calculate the min path cost to every other points after the tp's are found
#the function goes to every column in every row of the lists
def fillTheRest(list1,list2):
    for indexJ in range (1,len(list1)):
        for indexI in range(1,len(list1)):
            if list1[indexJ][indexI]==0: #if the value of list1 in that point is 0 it means it hasnt been already calculated
                list1[indexJ][indexI]=list2[indexJ][indexI]+min(list1[indexJ-1][indexI],list1[indexJ][indexI-1])

#the function is used to return the optimal solution as an integer
def returnSolution(list1):
    mazeSolution = list1[10][10]
    return mazeSolution

#the function is used to find the minimum cost path's value to reach the finish tile
def leastCostPath(list1, list2):
    sumCostPathRow(list1[0], list2[0])
    sumCostPathCol(list1, list2)

    (xFirstTp, yFirstTp)=fillToFirstTP(list1, list2) #the coordinates of the first tp are stored
    (xSecondTp, ySecondTp)=fillToLastTP(xFirstTp,list1,list2,tpCoords) #the coordinates of the second tp are stored

    #the value of the tp's will be the minimum cost of the path to the other tp tile
    #for ex is the min cost path to the first tp is 12, when the first tp is used, the value of the 2nd teleport will be 12
    list1[xFirstTp][yFirstTp]=min(list1[xSecondTp-1][ySecondTp], list1[xSecondTp][ySecondTp-1])
    list1[xSecondTp][ySecondTp]=min(list1[xFirstTp-1][yFirstTp], list1[xFirstTp][yFirstTp-1])
    print(list1[xFirstTp][yFirstTp],list1[xSecondTp][ySecondTp])

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
    pathsCoordinates.append([indexJ, indexI]) #whenever a new path is found its starting point is stored in a list

#the function is used to find the previous tile of the path after calculating the value of the min cost path
def findPreviousTile(list1, list2, indexJ, indexI):
    if list1[indexJ-1][indexI] == list1[indexJ][indexI-1]: #if the value of the tile to the left and the one above are equal
        if list2[indexJ - 1][indexI] == list2[indexJ][indexI - 1]: #the penalty points of the tiles are tested and, if they are equal
            remindPossiblePath(indexJ,indexI-1) #it means there is another possible path
            return (indexJ - 1, indexI)
        elif list2[indexJ-1][indexI] > list2[indexJ][indexI-1]: #if the value of the penalty points of the above tile are greater
            return (indexJ-1, indexI) #return the coordinates of the above tile
        else: # else return the coordinates of the tile adjacent to the left
            return(indexJ, indexI-1)
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
theMaze=createMaze()
minPathCost=list(np.zeros((11,11)))

leastCostPath(minPathCost, theMaze) #the value of the least cost path is calculated
optimalSolution=returnSolution(minPathCost) #the value is stored in a variable

mazePath.append(findPaths(minPathCost,theMaze,10,10)) #the first path is calculated

for indexJ in range(0,len(pathsCoordinates)): #for every list of coordinates in pathsCoordinates
    mazePath.append(findPaths(minPathCost, theMaze, pathsCoordinates[indexJ][0],pathsCoordinates[indexJ][1])) #the other possible paths
    #are stored
