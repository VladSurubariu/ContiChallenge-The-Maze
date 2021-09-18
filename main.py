import pygame
import os
import mazeSolve
import guiFunctions

pygame.font.init()

MAZE_SOLUTION=mazeSolve.optimalSolution
THE_MAZE=mazeSolve.theMaze

WIDTH, HEIGHT=900, 700
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUNDCOLOR=(240,255,240) #mintcream

FPS=60

CURRENT_POSITION=(50,150)
CELL_SIZE=(40,40)
CELL_DISTANCE_LINE=(35,0)
CELL_DISTANCE_ROW=(0,35)

BLACK_SQUARE_TILE_IMAGE=pygame.image.load(os.path.join('resources','blacksquare.png'))
WHITE_SQUARE_TILE_IMAGE=pygame.image.load(os.path.join('resources','whitesquare.png'))
GRAY_SQUARE_TILE_IMAGE=pygame.image.load(os.path.join('resources','graysquare.png'))
START_SQUARE_TILE_IMAGE=pygame.image.load(os.path.join('resources','startsquare.png'))
TP_SQUARE_TILE_IMAGE=pygame.image.load(os.path.join('resources','tpsquare.png'))

BLACK_SQUARE_TILE=pygame.transform.scale(BLACK_SQUARE_TILE_IMAGE,CELL_SIZE)
WHITE_SQUARE_TILE=pygame.transform.scale(WHITE_SQUARE_TILE_IMAGE,CELL_SIZE)
GRAY_SQUARE_TILE=pygame.transform.scale(GRAY_SQUARE_TILE_IMAGE,CELL_SIZE)
START_SQUARE_TILE=pygame.transform.scale(START_SQUARE_TILE_IMAGE,CELL_SIZE)
TP_SQUARE_TILE=pygame.transform.scale(TP_SQUARE_TILE_IMAGE, CELL_SIZE)

FONT=pygame.font.SysFont("monospane",40)

START_LABEL=FONT.render("S",1,(0,0,0))
START_LABEL_POSITION=(65, 158)
FINISH_LABEL=FONT.render("X",1,(0,0,0))
FINISH_LABEL_POSITION=(462, 560)

MAZE_MARGIN_POSITION=(48,148)
MAZE_MARGIN_SIZE=(444,444)


pygame.display.set_caption("The ContiChallenge Maze")

def drawTiles(maze):
    global CURRENT_POSITION
    for indexJ in range(0,len(maze)):
        for indexI in range(0,len(maze)):
            #print(CURRENT_POSITION)
            if maze[indexJ][indexI] == 0:
                pygame.draw.rect(WIN,(248,248,248),pygame.Rect(CURRENT_POSITION,CELL_SIZE))
                if indexJ ==0 and indexI==0:
                    WIN.blit(START_LABEL,START_LABEL_POSITION)
                elif indexJ==10 and indexI==10:
                    WIN.blit(FINISH_LABEL, FINISH_LABEL_POSITION)
            elif maze[indexJ][indexI] == 1:
               pygame.draw.rect(WIN, (248,248,248), pygame.Rect(CURRENT_POSITION, CELL_SIZE))
            elif maze[indexJ][indexI] == 2:
                pygame.draw.rect(WIN, (211,211,211), pygame.Rect(CURRENT_POSITION, CELL_SIZE))
            elif maze[indexJ][indexI] == 3:
                pygame.draw.rect(WIN, (40,40,40), pygame.Rect(CURRENT_POSITION, CELL_SIZE))
            elif maze[indexJ][indexI] == 4:
                pygame.draw.rect(WIN, (176,224,230), pygame.Rect(CURRENT_POSITION, CELL_SIZE))

            if indexI == 10:
                CURRENT_POSITION= guiFunctions.sumUpTuples(CURRENT_POSITION,(-400,40))
            else :
                CURRENT_POSITION = guiFunctions.sumUpTuples(CURRENT_POSITION, (40, 0))
    CURRENT_POSITION=(50,150)

def drawWindow():
    WIN.fill(BACKGROUNDCOLOR)
    pygame.draw.rect(WIN, (40,40,40), pygame.Rect(MAZE_MARGIN_POSITION, MAZE_MARGIN_SIZE))
    drawTiles(THE_MAZE)
    pygame.display.update()


def main():
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        drawWindow()

    pygame.quit()

if __name__=="__main__":
    main()