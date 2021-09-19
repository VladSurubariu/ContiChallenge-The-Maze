#Conti Challenge-The Maze

import numpy as np

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

def sumCostPathRow(list1,list2):
    for index in range(1,len(list1)):
        list1[index]=list1[index-1]+list2[index]

def sumCostPathCol(list1,list2):
    for index in range(1,len(list1)):
        list1[index][0]=list1[index-1][0]+list2[index][0]

def fillToFirstTP(list1, list2):
    for indexJ in range (1,len(list1)):
        for indexI in range(1,len(list1)):
            if list2[indexJ][indexI] !=4:
                list1[indexJ][indexI]=list2[indexJ][indexI]+min(list1[indexJ-1][indexI],list1[indexJ][indexI-1])
            else:
                tpCoords.append([indexJ,indexI])
                return (indexJ,indexI)

def fillToLastTP(x,list1, list2):
    for indexJ in range(1,len(list1)):
        for indexI in range(x,len(list1)):
            if list2[indexI][indexJ] !=4:
                list1[indexI][indexJ]=list2[indexI][indexJ]+min(list1[indexI-1][indexJ],list1[indexI][indexJ-1])
            else:
                tpCoords.append([indexI,indexJ])
                return (indexI,indexJ)

def fillTheRest(list1,list2):
    for indexJ in range (1,len(list1)):
        for indexI in range(1,len(list1)):
            if list1[indexJ][indexI]==0:
                list1[indexJ][indexI]=list2[indexJ][indexI]+min(list1[indexJ-1][indexI],list1[indexJ][indexI-1])

def returnSolution(list1):
    mazeSolution = list1[10][10]
    #print(f'The min cost solution is: {int(mazeSolution)}')
    return mazeSolution

def leastCostPath(list1, list2):
    sumCostPathRow(list1[0], list2[0])
    sumCostPathCol(list1, list2)

    (xFirstTp, yFirstTp)=fillToFirstTP(list1, list2)
    (xSecondTp, ySecondTp)=fillToLastTP(xFirstTp,list1,list2)
    list1[xFirstTp][yFirstTp]=min(list1[xSecondTp-1][ySecondTp], list1[xSecondTp][ySecondTp-1])
    list1[xSecondTp][ySecondTp]=min(list1[xFirstTp-1][yFirstTp], list1[xFirstTp][yFirstTp-1])

    fillTheRest(list1, list2)

def checkTeleportTile(list2, indexJ, indexI):
    global tpCoords
    if list2[indexJ][indexI] == 4:
        if indexJ==tpCoords[0][0] and indexI==tpCoords[0][1]:
            indexJ=tpCoords[1][0]
            indexI=tpCoords[1][1]
        elif indexJ==tpCoords[1][0] and indexI==tpCoords[1][1]:
            indexJ=tpCoords[0][0]
            indexI=tpCoords[0][1]
        return (indexJ, indexI)
    return False


def remindPossiblePath(indexJ, indexI):
    global pathsCoordinates
    pathsCoordinates.append([indexJ, indexI])
    #print(pathsCoordinates)

def findPreviousTile(list1, list2, indexJ, indexI):
    if list1[indexJ-1][indexI] == list1[indexJ][indexI-1]:
        if list2[indexJ - 1][indexI] == list2[indexJ][indexI - 1]:
            remindPossiblePath(indexJ,indexI-1)
            return (indexJ - 1, indexI)
        elif list2[indexJ-1][indexI] > list2[indexJ][indexI-1]:
            return (indexJ-1, indexI)
        else:
            return(indexJ, indexI-1)
    else:
        if(list1[indexJ-1][indexI]<list1[indexJ][indexI-1]):
            return(indexJ-1, indexI)
        else:
            return(indexJ, indexI-1)


def findPaths(list1, list2, indexJ, indexI):
    pathList=[]
    while indexJ!=0 or indexI!=0:
        pathList.append([indexJ, indexI])
        if checkTeleportTile(list2, indexJ, indexI):
            (indexJ,indexI)=checkTeleportTile(list2,indexJ,indexI)
            pathList.append([indexJ,indexI])
        (indexJ,indexI)=findPreviousTile(list1,list2,indexJ, indexI)
    pathList.append([indexJ, indexI])

    return pathList

#main

tpCoords=[]
pathsCoordinates=[]
mazePath=[]
theMaze=createMaze()

minPathCost=list(np.zeros((11,11)))
leastCostPath(minPathCost, theMaze)
optimalSolution=returnSolution(minPathCost)

mazePath.append(findPaths(minPathCost,theMaze,10,10))

for indexJ in range(0,len(pathsCoordinates)):
    mazePath.append(findPaths(minPathCost, theMaze, pathsCoordinates[indexJ][0],pathsCoordinates[indexJ][1]))

#print(mazePath)