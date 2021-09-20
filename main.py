import pygame
import mazeSolve
import guiFunctions

#importing from the other .py files and initialising constants

pygame.font.init()  #initialising the fonts
MAZE_SOLUTION=mazeSolve.optimalSolution #importing the maze solution
THE_MAZE=mazeSolve.theMaze #importing the maze tiles values
THE_PATHS_LIST=mazeSolve.mazePath #importing the paths Coordinates

WIDTH, HEIGHT=900, 700 #the witdth and height of the GUI
WIN=pygame.display.set_mode((WIDTH,HEIGHT)) #creating the GUI

#Colors
BACKGROUNDCOLOR=(240,255,240) #mintcream
BLACK=(0,0,0)
WHITE_SMOKE=(248,248,248)
LIGHT_GRAY=(211,211,211)
NERO_BLACK=(40,40,40)
POWDER_BLUE=(176,224,230)
KELLY_GREEN=(76, 187, 23)

FPS=60

current_position=(50,150) #current position. the place where the drawing will begin
CELL_SIZE=(40,40) #the size of the cell

FONT=pygame.font.Font('fonts/Gasalt-Black.ttf',40) #initialising the main font
TITLE_FONT=pygame.font.Font("fonts/Gamy.otf", 50) #initialising the title font

START_LABEL=FONT.render("S",1,BLACK) #initialising the S tile font
START_LABEL_POSITION=(63, 153) #initialising the S tile position
FINISH_LABEL=FONT.render("X",1,BLACK) #initialising the F tile font
FINISH_LABEL_POSITION=(462, 555) #initialising the S tile position

SCORE_LABEL=FONT.render("Searching for paths...",1,BLACK) #initialising the "Searching for paths" label
SCORE_LABEL_POSITION=(550, 300) #initialising the position
SCORE_LABEL_SIZE=(300,100) #initialising the square that will cover the "Searching for paths" label

score=str(int(mazeSolve.minPathCost[10][10])) #initialising the score string
score="The score is: "+score #initialising the score label
UPDATED_SCORE=FONT.render(score, 1, BLACK) #creating the label for the updated score
UPDATED_SCORE_POSITION=(550,300) #the updated score label position

MAZE_MARGIN_POSITION=(48,148) #the maze grid starting position
MAZE_MARGIN_SIZE=(444,444) #the maze grid size

PATH_SIZE_VERT=(10,20) #the path size if its vertically-oriented
PATH_SIZE_HORIZ=(20,10) #the path size if its horizontally-oriented
PATH_SIZE_BRANCH=(10,10) #the path if its another starting point of another possible path

TITLE_LABEL_POSITION=(280,50) #the title label position
TITLE_LABEL=TITLE_FONT.render("The Conti Maze", 1, BLACK) #initialising the title label

animationsTimeCounter=0 #counts the number of times when the path animation took place

pygame.display.set_caption("The Conti Maze") #modifying the window caption

# the function returns a value depeding on the previous path point's coordinates
def decideOrientationPrevious(pathsList, indexJ, indexI):
    if pathsList[indexJ][indexI]==[0,0] or pathsList[indexJ][indexI]==[10,10]: #if its the Start or the Finish of the path
        return False
    elif pathsList[indexJ][indexI][0] < pathsList[indexJ][indexI-1][0]: #if the path goes vertical
        return 1
    elif pathsList[indexJ][indexI][0] == pathsList[indexJ][indexI-1][0]: #if the path goes horizontal
        return 2

def searchForOrientation(maze,indexJ,indexI,pathTileCoordinates,pathsList):
    element=pathsList[indexJ][indexI]
    for list in maze:
        for listElement in list:
            if element[0]==listElement[0]-1 and element[1]==listElement[1]:
                pygame.draw.rect(WIN, KELLY_GREEN, pygame.Rect(pathTileCoordinates, PATH_SIZE_VERT))  # the path tile is drawn vertically
            #if element[0]==listElement[0]+1 and element[1]==listElement[1]:
                #pygame.draw.rect(WIN, KELLY_GREEN,pygame.Rect(pathTileCoordinates, PATH_SIZE_VERT))  # the path tile is drawn vertically
            if element[0]==listElement[0] and element[1]==listElement[1]-1:
                pygame.draw.rect(WIN, KELLY_GREEN, pygame.Rect(pathTileCoordinates, PATH_SIZE_HORIZ))  # the path tile is drawn horizontally
            if element[0]==listElement[0] and element[1]==listElement[1]+1:
                pygame.draw.rect(WIN, KELLY_GREEN, pygame.Rect(pathTileCoordinates, PATH_SIZE_HORIZ))  # the path tile is drawn horizontally

#the function draws the most optimal path/paths
def drawPaths(maze, pathsList):
    current_position=(65,160) #this is the place where the path is starting from
    global animationsTimeCounter
    animationsTimeCounter+=1 #after every call of the function the animationTimeCounter will increase
    for indexJ in range(0,len(pathsList)): #for every list in the pathList
        for indexI in range(len(pathsList[indexJ])-1,-1,-1): #going from last to first point in the pathList[indexI]
            if animationsTimeCounter==1: #if its the first time the function is called, the animations takes place
                pygame.time.delay(200) #the delay function is called in order to give the impression of an animation
                pygame.display.update() #the windows is updated
            y,x=pathsList[indexJ][indexI] #y and x take the pathpoint coordinates
            pathTileCoordinates=(x*40+current_position[0],y*40+current_position[1]) #updating the current coordinates of the pathpoint
            orientation=decideOrientationPrevious(pathsList, indexJ, indexI)
            if orientation == 1 : #if the previous pathpoint was above the current pathpoint
                pygame.draw.rect(WIN, KELLY_GREEN, pygame.Rect(pathTileCoordinates, PATH_SIZE_VERT)) #the path tile is drawn vertically
            elif orientation == 2: #if the previous pathpoint was to the left of the current pathpoint
                pygame.draw.rect(WIN, KELLY_GREEN, pygame.Rect(pathTileCoordinates, PATH_SIZE_HORIZ)) #the path tile is drawn horizontally
            elif orientation == None: #if there are no previous pathpoint it means that this is an alternate route
                searchForOrientation(maze, indexJ, indexI, pathTileCoordinates, pathsList)

#the function colors the tile depending on the value of the penalty points the tile has
def decideTileType(maze, indexJ, indexI, currentPosition):
    if maze[indexJ][indexI] == 0: #if the penalty point has value 0 it means its the start or the finish point
        pygame.draw.rect(WIN, WHITE_SMOKE, pygame.Rect(current_position, CELL_SIZE)) #a white tile is drawn
        if indexJ == 0 and indexI == 0: #the start tile is drawn
            WIN.blit(START_LABEL, START_LABEL_POSITION)
        elif indexJ == 10 and indexI == 10: #the finish tile is drawn
            WIN.blit(FINISH_LABEL, FINISH_LABEL_POSITION)
    elif maze[indexJ][indexI] == 1: #if the penalty point has value 1 it means its a white tile
        pygame.draw.rect(WIN, WHITE_SMOKE, pygame.Rect(current_position, CELL_SIZE))
    elif maze[indexJ][indexI] == 2: #if the penalty point has value 2 it means its a gray tile
        pygame.draw.rect(WIN, LIGHT_GRAY, pygame.Rect(current_position, CELL_SIZE))
    elif maze[indexJ][indexI] == 3: #if the penalty point has value 3 it means its a black tile
        pygame.draw.rect(WIN, NERO_BLACK, pygame.Rect(current_position, CELL_SIZE))
    elif maze[indexJ][indexI] == 4: #if the penalty point has value 4 it means its a teleporter tile
        pygame.draw.rect(WIN, POWDER_BLUE, pygame.Rect(current_position, CELL_SIZE))

#the function draws the tiles
def drawTiles(maze):
    global current_position
    for indexJ in range(0,len(maze)):
        for indexI in range(0,len(maze)):
            decideTileType(maze,indexJ,indexI,current_position) #deciding and coloring the maze tiles
            if indexI == 10: #at the end of every row the tiles will continue to be drawn from the beginning of the next row
                current_position= guiFunctions.sumUpTuples(current_position,(-400,40))
            else : #else the currentposition is going to the right
                current_position = guiFunctions.sumUpTuples(current_position, (40, 0))
    current_position=(50,150)

#the function is used to update the score after the paths are drawn
def updateScore():
    pygame.draw.rect(WIN, BACKGROUNDCOLOR, pygame.Rect(SCORE_LABEL_POSITION, SCORE_LABEL_SIZE)) #drawing the score label
    WIN.blit(UPDATED_SCORE, UPDATED_SCORE_POSITION) #drawing the new label that contains the sum of the penalty points

#the function is used to draw the main elements of the window
def drawWindow():
    global animationsTimeCounter
    WIN.fill(BACKGROUNDCOLOR) #coloring the background
    WIN.blit(TITLE_LABEL, TITLE_LABEL_POSITION) #drawing the label
    WIN.blit(SCORE_LABEL, SCORE_LABEL_POSITION) #drawing the "Searching for paths..." label
    pygame.draw.rect(WIN, (40,40,40), pygame.Rect(MAZE_MARGIN_POSITION, MAZE_MARGIN_SIZE)) #drawing the margin of the maze
    drawTiles(THE_MAZE) #drawing the tiles
    if animationsTimeCounter == 1: #if the animation took place the window is refreshed
        pygame.display.update()
    drawPaths(mazeSolve.mazePath,THE_PATHS_LIST) #the paths are drawn
    updateScore() #the score is updated
    pygame.display.update() #the window is updated again in order to include the last window elements

#the main function
def main():
    clock=pygame.time.Clock() #initialising clock in order to limit the fps
    run=True
    while run:
        clock.tick(FPS) #the fps are limited
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if the exit button is pressed
                run = False #the run variable is false and the while will stop
        drawWindow() #the drawing function is called
    pygame.quit() #the app is closed


if __name__=="__main__":
    main()