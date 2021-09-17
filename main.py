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
                return (indexJ,indexI)

def fillToLastTP(x,list1, list2):
    for indexJ in range(1,len(list1)):
        for indexI in range(x,len(list1)):
            if list2[indexI][indexJ] !=4:
                list1[indexI][indexJ]=list2[indexI][indexJ]+min(list1[indexI-1][indexJ],list1[indexI][indexJ-1])
            else:
                return (indexI,indexJ)

def fillTheRest(list1,list2):
    for indexJ in range (1,len(list1)):
        for indexI in range(1,len(list1)):
            if list1[indexJ][indexI]==0:
                list1[indexJ][indexI]=list2[indexJ][indexI]+min(list1[indexJ-1][indexI],list1[indexJ][indexI-1])

    return list1[10][10]

def leastCostPath(list1, list2):
    sumCostPathRow(list1[0], list2[0])
    sumCostPathCol(list1, list2)

    (xFirstTp, yFirstTp)=fillToFirstTP(list1, list2)
    (xSecondTp, ySecondTp)=fillToLastTP(xFirstTp,list1,list2)
    list1[xFirstTp][yFirstTp]=min(list1[xSecondTp-1][ySecondTp], list1[xSecondTp][ySecondTp-1])
    list1[xSecondTp][ySecondTp]=min(list1[xFirstTp-1][yFirstTp], list1[xFirstTp][yFirstTp-1])

    mazeSolution=fillTheRest(list1,list2)
    print(f'The min cost solution is: {int(mazeSolution)}')

#main

theMaze=createMaze()
minPathCost=list(np.zeros((11,11)))
leastCostPath(minPathCost, theMaze)
