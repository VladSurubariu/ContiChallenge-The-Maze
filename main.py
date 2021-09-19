import pygame
import os
import mazeSolve
import guiFunctions

pygame.font.init()
MAZE_SOLUTION=mazeSolve.optimalSolution
THE_MAZE=mazeSolve.theMaze
THE_PATHS_LIST=mazeSolve.mazePath

WIDTH, HEIGHT=900, 700
WIN=pygame.display.set_mode((WIDTH,HEIGHT))

#Colors
BACKGROUNDCOLOR=(240,255,240) #mintcream
BLACK=(0,0,0)
WHITE_SMOKE=(248,248,248)
LIGHT_GRAY=(211,211,211)
NERO_BLACK=(40,40,40)
POWDER_BLUE=(176,224,230)
KELLY_GREEN=(76, 187, 23)

FPS=60

current_position=(50,150)
CELL_SIZE=(40,40)

FONT=pygame.font.Font('fonts/Gasalt-Black.ttf',40)
TITLE_FONT=pygame.font.Font("fonts/Gamy.otf", 50)

START_LABEL=FONT.render("S",1,(0,0,0))
START_LABEL_POSITION=(63, 153)
FINISH_LABEL=FONT.render("X",1,(0,0,0))
FINISH_LABEL_POSITION=(462, 555)

MAZE_MARGIN_POSITION=(48,148)
MAZE_MARGIN_SIZE=(444,444)

PATH_SIZE_VERT=(10,20)
PATH_SIZE_HORIZ=(20,10)
PATH_SIZE_BRANCH=(10,10)

TITLE_LABEL_POSITION=(280,50)
TITLE_LABEL=TITLE_FONT.render("The Conti Maze", 1, BLACK)

animationsTimeCounter=0

pygame.display.set_caption("The Conti Maze")

def decideOrientationPrevious(pathsList, indexJ, indexI):
    #print(pathsList[indexJ][indexI],indexJ, indexI)
    if pathsList[indexJ][indexI]==[0,0] or pathsList[indexJ][indexI]==[10,10]:
        return False
    elif pathsList[indexJ][indexI][0] < pathsList[indexJ][indexI-1][0]:
        return 1
    elif pathsList[indexJ][indexI][0] == pathsList[indexJ][indexI-1][0]:
        return 2

def drawPaths(pathsList):
    current_position=(65,160)
    global animationsTimeCounter
    animationsTimeCounter+=1
    for indexJ in range(0,len(pathsList)):
        for indexI in range(0, len(pathsList[indexJ])):
            if animationsTimeCounter==1:
                pygame.time.delay(200)
                pygame.display.update()
            y,x=pathsList[indexJ][indexI]
            pathTileCoordinates=(x*40+current_position[0],y*40+current_position[1])
            orientation=decideOrientationPrevious(pathsList, indexJ, indexI)
            if orientation == 1 :
                pygame.draw.rect(WIN, KELLY_GREEN, pygame.Rect(pathTileCoordinates, PATH_SIZE_VERT))
            elif orientation == 2:
                pygame.draw.rect(WIN, KELLY_GREEN, pygame.Rect(pathTileCoordinates, PATH_SIZE_HORIZ))
            elif orientation == None:
                pygame.draw.rect(WIN, KELLY_GREEN, pygame.Rect(pathTileCoordinates, PATH_SIZE_BRANCH))


def decideTileColor(maze, indexJ, indexI, currentPosition):
    if maze[indexJ][indexI] == 0:
        pygame.draw.rect(WIN, WHITE_SMOKE, pygame.Rect(current_position, CELL_SIZE))
        if indexJ == 0 and indexI == 0:
            WIN.blit(START_LABEL, START_LABEL_POSITION)
        elif indexJ == 10 and indexI == 10:
            WIN.blit(FINISH_LABEL, FINISH_LABEL_POSITION)
    elif maze[indexJ][indexI] == 1:
        pygame.draw.rect(WIN, WHITE_SMOKE, pygame.Rect(current_position, CELL_SIZE))
    elif maze[indexJ][indexI] == 2:
        pygame.draw.rect(WIN, LIGHT_GRAY, pygame.Rect(current_position, CELL_SIZE))
    elif maze[indexJ][indexI] == 3:
        pygame.draw.rect(WIN, NERO_BLACK, pygame.Rect(current_position, CELL_SIZE))
    elif maze[indexJ][indexI] == 4:
        pygame.draw.rect(WIN, POWDER_BLUE, pygame.Rect(current_position, CELL_SIZE))

def drawTiles(maze):
    global current_position
    for indexJ in range(0,len(maze)):
        for indexI in range(0,len(maze)):
            #print(current_position)
            decideTileColor(maze,indexJ,indexI,current_position)
            if indexI == 10:
                current_position= guiFunctions.sumUpTuples(current_position,(-400,40))
            else :
                current_position = guiFunctions.sumUpTuples(current_position, (40, 0))
    current_position=(50,150)


def drawWindow():
    global animationsTimeCounter
    WIN.fill(BACKGROUNDCOLOR)
    WIN.blit(TITLE_LABEL, TITLE_LABEL_POSITION)
    pygame.draw.rect(WIN, (40,40,40), pygame.Rect(MAZE_MARGIN_POSITION, MAZE_MARGIN_SIZE))
    drawTiles(THE_MAZE)
    if animationsTimeCounter == 1:
        pygame.display.update()
    drawPaths(THE_PATHS_LIST)
    pygame.display.update()

def main():
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        drawWindow()
    pygame.quit()


if __name__=="__main__":
    main()