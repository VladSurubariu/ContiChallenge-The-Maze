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
BUTTONS_FONT=pygame.font.Font('fonts/Gasalt-Black.ttf',20)
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
UPDATED_SCORE_POSITION=(570,300) #the updated score label position

MAZE_MARGIN_POSITION=(48,148) #the maze grid starting position
MAZE_MARGIN_SIZE=(444,444) #the maze grid size

PATH_SIZE_VERT=(10,20) #the path size if its vertically-oriented
PATH_SIZE_HORIZ=(20,10) #the path size if its horizontally-oriented
PATH_SIZE_BRANCH=(10,10) #the path if its another starting point of another possible path

TITLE_LABEL_POSITION=(280,50) #the title label position
TITLE_LABEL=TITLE_FONT.render("The Conti Maze", 1, BLACK) #initialising the title label

OPTION_SELECT_LABEL=BUTTONS_FONT.render("How many paths do you want to see?",1,BLACK) #a label
MULTIPLE_PATHS_LABEL=BUTTONS_FONT.render("ALL PATHS", 1, BLACK) #label for the "ALL PATHS" button
ONE_PATH_LABEL=BUTTONS_FONT.render("ONE PATH",1,BLACK) #label for the "ONE PATH BUTTON"
OPTION_SELECT_LABEL_POSITION=(550,400) #"how many paths do you want to see?" label's position
MULTIPLE_PATHS_LABEL_POSITION=(700,450) #all paths button's position
ONE_PATH_LABEL_POSITION=(590,450) #one path button's position

BUTTONS_SIZE=(90,20) #the size of the buttons
BUTTONS_MARGIN_SIZE=(92,22) #the size of the margin of the buttons
FIRST_BUTTON_MARGIN_POSITION=(584,449) #the position of the first button margin
SECOND_BUTTON_MARGIN_POSITION=(694,449) #the position of the second button margin

animationsTimeCounter=0 #counts the number of times when the path animation took place

class Button():
    # when a button is initialised
    def __init__(self,position,label):
        self.label=label
        self.rect=self.label.get_rect() #initialising the rect object in order to use the topleft method
        self.rect.topleft=(position[0],position[1]) #topleft method to store coordinates
        self.clicked= False

    #when a button is drawn
    def draw(self):
        action=False #initialisation
        pygame.draw.rect(WIN, POWDER_BLUE, pygame.Rect((self.rect.x-5, self.rect.y),BUTTONS_SIZE)) #the background of the button is drawn
        WIN.blit(self.label, (self.rect.x, self.rect.y)) #the label of the button is drawn

        pos=pygame.mouse.get_pos() #used to get the mouse position
        if self.rect.collidepoint(pos): #if the mouse position is hovering the button
            if pygame.mouse.get_pressed()[0] ==1 and self.clicked == False: #if the button was pressed
                self.clicked=True #clicked variable is true
                action=True #action is triggered
        if pygame.mouse.get_pressed()[0]==0: #if its nor pressed anymore
            self.clicked=False #clicked variable is false

        return action

ONE_PATH_BUTTON=Button(ONE_PATH_LABEL_POSITION, ONE_PATH_LABEL) #the "one path" button initialisation
MULTIPLE_PATHS_BUTTON=Button(MULTIPLE_PATHS_LABEL_POSITION,MULTIPLE_PATHS_LABEL) #the "all paths" button initialisation

pygame.display.set_caption("The Conti Maze") #modifying the window caption

#the function is drawing the tiles of the path according to the orientation of the path
def drawAccordingToOrientation(orientation,pathTileCoordinates,indexJ, indexI, pathsList,color):
    if orientation == 1:  # if the previous pathpoint was above the current pathpoint
        pygame.draw.rect(WIN, color,
                         pygame.Rect(pathTileCoordinates, PATH_SIZE_VERT))  # the path tile is drawn vertically
    elif orientation == 2:  # if the previous pathpoint was to the left of the current pathpoint
        pygame.draw.rect(WIN, color,
                         pygame.Rect(pathTileCoordinates, PATH_SIZE_HORIZ))  # the path tile is drawn horizontally
    elif orientation == None:  # if there are no previous pathpoint it means that this is an alternate route
        searchForSpecialOrientation(indexJ, indexI, pathTileCoordinates, pathsList,color)

# the function returns a value depeding on the previous path point's coordinates
def decideOrientationPrevious(pathsList, indexJ, indexI,current_position,color):
    if pathsList[indexJ][indexI]==[0,0] or pathsList[indexJ][indexI]==[10,10]: #if its the Start or the Finish of the path
        orientation=False
    elif pathsList[indexJ][indexI][0] < pathsList[indexJ][indexI-1][0]: #if the path goes vertical
        orientation=1
    elif pathsList[indexJ][indexI][0] == pathsList[indexJ][indexI-1][0]: #if the path goes horizontal
        orientation=2
    else: #if there can't be estabilished an orientation
        orientation=None
    y, x = pathsList[indexJ][indexI]  # y and x take the pathpoint coordinates
    pathTileCoordinates = (x * 40 + current_position[0], y * 40 + current_position[1]) #the starting point of the drawing
    drawAccordingToOrientation(orientation,pathTileCoordinates,indexJ,indexI, pathsList, color) #the drawing accordint to path orientation

#the function is searching for the path's orientation before drawing it
def searchForSpecialOrientation(indexJ,indexI,pathTileCoordinates,pathsList, color):
    element=pathsList[indexJ][indexI] #the tuple were the coordinates of the path are stored
    for list in pathsList:
        for listElement in list:
            if element[0]==listElement[0]-1 and element[1]==listElement[1]: #if the previous path element was above
                pygame.draw.rect(WIN, color, pygame.Rect(pathTileCoordinates, PATH_SIZE_VERT))  # the path tile is drawn vertically
            #if element[0]==listElement[0]+1 and element[1]==listElement[1]: #if the previous path element was below
                #pygame.draw.rect(WIN, KELLY_GREEN,pygame.Rect(pathTileCoordinates, PATH_SIZE_VERT))  # the path tile is drawn vertically
            if element[0]==listElement[0] and element[1]==listElement[1]-1: #if the previous path element was to the left
                pygame.draw.rect(WIN, color, pygame.Rect(pathTileCoordinates, PATH_SIZE_HORIZ))  # the path tile is drawn horizontally
            if element[0]==listElement[0] and element[1]==listElement[1]+1: #if the previous path elemnet was to the right
                pygame.draw.rect(WIN, color, pygame.Rect(pathTileCoordinates, PATH_SIZE_HORIZ))  # the path tile is drawn horizontally

#the function draws the most optimal path/paths
def drawPaths(pathsList, color, drawMainPathBool):
    current_position=(65,160) #this is the place where the path is starting from
    global animationsTimeCounter
    animationsTimeCounter+=1 #after every call of the function the animationTimeCounter will increase
    for indexJ in range(0,len(pathsList)): #for every list in the pathList
        for indexI in range(len(pathsList[indexJ])-1,-1,-1): #going from last to first point in the pathList[indexI]
            if animationsTimeCounter==1: #if its the first time the function is called, the animations takes place
                pygame.time.delay(200) #the delay function is called in order to give the impression of an animation
                pygame.display.update() #the windows is updated

             #updating the current coordinates of the pathpoint
            decideOrientationPrevious(pathsList, indexJ, indexI,current_position,color)
        if drawMainPathBool==1: #if the user only wants to draw the main path this if will be triggered
            return 0 #and a return will be made to stop drawing the other paths

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

#the function draws the options buttons and draws the path/paths according to the user's input
def drawOptionsButtons():
    pygame.draw.rect(WIN, BLACK, pygame.Rect(FIRST_BUTTON_MARGIN_POSITION, BUTTONS_MARGIN_SIZE)) #one path button is drawn
    if ONE_PATH_BUTTON.draw(): #if the button is drawn
        drawTiles(THE_MAZE) #the maze is drawn again
        drawPaths(THE_PATHS_LIST,KELLY_GREEN,1) #only the main path is drawn because the 3rd parameter is 1
        pygame.display.update() #an update is made to the display in order to print the new elements

    pygame.draw.rect(WIN, BLACK, pygame.Rect(SECOND_BUTTON_MARGIN_POSITION, BUTTONS_MARGIN_SIZE)) #all paths button is drawn
    if MULTIPLE_PATHS_BUTTON.draw(): #if the button is drawn
        drawPaths(THE_PATHS_LIST, KELLY_GREEN,0)  # all paths are drawn because the 3rd parameter is 0
        pygame.display.update() #an update is made to the display in order to print the new elements

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

    drawPaths(THE_PATHS_LIST, KELLY_GREEN,0) #the paths are drawn
    updateScore() #the score is updated
    WIN.blit(OPTION_SELECT_LABEL, OPTION_SELECT_LABEL_POSITION) #the "select option" label is drawn
    drawOptionsButtons() #the options drawing function is called
    pygame.display.update() #the window is updated again in order to include the last window elements

#the main function
def main():
    clock=pygame.time.Clock() #initialising clock in order to limit the fps
    run=True
    drawingOption=0
    while run:
        clock.tick(FPS) #the fps are limited
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if the exit button is pressed
                run = False #the run variable is false and the while will stop
        if drawingOption==0: #local variable that only has value 1 at the first call of the main function
            drawWindow() #the drawing function is called
            drawingOption=1 #drawingOption becomes 1 because only drawOptionsButtons() function is needed from now on
        else: #after the first call every call of the main() will execute this else
            drawOptionsButtons() #the function is called until the user closes the program
    pygame.quit() #the app is closed


if __name__=="__main__":
    main()