# Tic Tac Toe

import pygame, sys, random
from pygame.locals import *

# Create the constants (go ahead and experiment with different values)
BOARDWIDTH = 3  # number of columns in the board
BOARDHEIGHT = 3 # number of rows in the board
TILESIZE = 80
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
PINK = (255, 180, 160)
RED = (255,0,0)
BLUE = (0,0,255)
GRAY = (128, 128, 128)
PURPLE = (200, 0, 200)


BGCOLOR = BLACK
LIGHTBGCOLOR = GRAY
TILECOLOR = PINK
TEXTCOLOR = WHITE
BORDERCOLOR = WHITE
BASICFONTSIZE = 30

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE
LINECOLOR = PURPLE

XCOLOR = RED
OCOLOR = BLUE

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, NEW_SURF, NEW_RECT, PLAYER, MESSAGE, revealedBoxes, currentBoard

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Tic Tac Toe')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    MESSAGE = ''



    # Store the option buttons and their rectangles in OPTIONS.
    NEW_SURF,   NEW_RECT   = makeText('Main Menu', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60)
    
    numOfPlayers = showStartScreen()
    #currentBoard = getStartingBoard()
    #revealedBoxes = generateRevealedBoxesData(False)


    while True: # main game loop
	#runGame()
        #showGameOverScreen()
        DISPLAYSURF.fill(BGCOLOR)
        currentBoard = getStartingBoard()
        revealedBoxes = generateRevealedBoxesData(False)
	drawBoard(currentBoard, revealedBoxes, MESSAGE)

	if numOfPlayers == 1:
	    numOfPlayers = runGameAgainstComp(currentBoard, revealedBoxes)
        elif numOfPlayers == 2:
            numOfPlayers = runTwoPlayerGame(currentBoard, revealedBoxes)

        checkForQuit()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def runGameAgainstComp(currentBoard, revealedBoxes):
    PLAYER = random.choice([1,2])
    if PLAYER == 1:
	MESSAGE = "It's your turn!"
    else:
	MESSAGE = "It's the computer's turn!"

    drawBoard(currentBoard, revealedBoxes, MESSAGE)
    pygame.display.update()
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        mousex = 0 
        mousey = 0
        boxx = None
        boxy = None
        drawBoard(currentBoard, revealedBoxes, MESSAGE)
        checkForQuit()
        if PLAYER == 2:
	    if revealedBoxes[0][0] == False and revealedBoxes[0][1] == PLAYER and revealedBoxes[0][2] == PLAYER:
		revealedBoxes[0][0] = PLAYER
	    elif revealedBoxes[0][0] == PLAYER and revealedBoxes[0][1] == False and revealedBoxes[0][2] == PLAYER:
		revealedBoxes[0][1] = PLAYER
	    elif revealedBoxes[0][0] == PLAYER and revealedBoxes[0][1] == PLAYER and revealedBoxes[0][2] == False:
		revealedBoxes[0][2] = PLAYER        
	    elif revealedBoxes[1][0] == False and revealedBoxes[1][1] == PLAYER and revealedBoxes[1][2] == PLAYER:
		revealedBoxes[1][0] = PLAYER
	    elif revealedBoxes[1][0] == PLAYER and revealedBoxes[1][1] == False and revealedBoxes[1][2] == PLAYER:
		revealedBoxes[1][1] = PLAYER
	    elif revealedBoxes[1][0] == PLAYER and revealedBoxes[1][1] == PLAYER and revealedBoxes[1][2] == False:
		revealedBoxes[1][2] = PLAYER
	    elif revealedBoxes[2][0] == False and revealedBoxes[2][1] == PLAYER and revealedBoxes[2][2] == PLAYER:
		revealedBoxes[2][0] = PLAYER
	    elif revealedBoxes[2][0] == PLAYER and revealedBoxes[2][1] == False and revealedBoxes[2][2] == PLAYER:
		revealedBoxes[2][1] = PLAYER
	    elif revealedBoxes[2][0] == PLAYER and revealedBoxes[2][1] == PLAYER and revealedBoxes[2][2] == False:
		revealedBoxes[2][2] = PLAYER  
	    elif revealedBoxes[0][0] == False and revealedBoxes[1][0] == PLAYER and revealedBoxes[2][0] == PLAYER:
		revealedBoxes[0][0] = PLAYER
	    elif revealedBoxes[0][0] == PLAYER and revealedBoxes[1][0] == False and revealedBoxes[2][0] == PLAYER:
		revealedBoxes[1][0] = PLAYER
	    elif revealedBoxes[0][0] == PLAYER and revealedBoxes[1][0] == PLAYER and revealedBoxes[2][0] == False:
		revealedBoxes[2][0] = PLAYER
	    elif revealedBoxes[0][1] == False and revealedBoxes[1][1] == PLAYER and revealedBoxes[2][1] == PLAYER:
		revealedBoxes[0][1] = PLAYER
	    elif revealedBoxes[0][1] == PLAYER and revealedBoxes[1][1] == False and revealedBoxes[2][1] == PLAYER:
		revealedBoxes[1][1] = PLAYER
	    elif revealedBoxes[0][1] == PLAYER and revealedBoxes[1][1] == PLAYER and revealedBoxes[2][1] == False:
		revealedBoxes[2][1] = PLAYER
	    elif revealedBoxes[0][2] == False and revealedBoxes[1][2] == PLAYER and revealedBoxes[2][2] == PLAYER:
		revealedBoxes[0][2] = PLAYER
	    elif revealedBoxes[0][2] == PLAYER and revealedBoxes[1][2] == False and revealedBoxes[2][2] == PLAYER:
		revealedBoxes[1][2] = PLAYER
	    elif revealedBoxes[0][2] == PLAYER and revealedBoxes[1][2] == PLAYER and revealedBoxes[2][2] == False:
		revealedBoxes[2][2] = PLAYER 
	    elif revealedBoxes[0][0] == False and revealedBoxes[1][1] == PLAYER and revealedBoxes[2][2] == PLAYER:
		revealedBoxes[0][0] = PLAYER
	    elif revealedBoxes[0][0] == PLAYER and revealedBoxes[1][1] == False and revealedBoxes[2][2] == PLAYER:
		revealedBoxes[1][1] = PLAYER
	    elif revealedBoxes[0][0] == PLAYER and revealedBoxes[1][1] == PLAYER and revealedBoxes[2][2] == False:
		revealedBoxes[2][2] = PLAYER       
	    elif revealedBoxes[2][0] == False and revealedBoxes[1][1] == PLAYER and revealedBoxes[0][2] == PLAYER:
		revealedBoxes[2][0] = PLAYER
	    elif revealedBoxes[2][0] == PLAYER and revealedBoxes[1][1] == False and revealedBoxes[0][2] == PLAYER:
		revealedBoxes[1][1] = PLAYER
	    elif revealedBoxes[2][0] == PLAYER and revealedBoxes[1][1] == PLAYER and revealedBoxes[0][2] == False:
		revealedBoxes[0][2] = PLAYER


            else:
    	        potentialMoves=[]

                for x in range(BOARDWIDTH):
                    for y in range(BOARDHEIGHT):
         	        if revealedBoxes[x][y] == False:
    		            potentialMoves.append((x,y))
                #if len(potentialMoves) != 0:
                (x,y) = random.choice(potentialMoves)
                revealedBoxes[x][y] = PLAYER
            pygame.time.wait(2000)

            if not hasWon(PLAYER, revealedBoxes) and not playersTied(revealedBoxes):   
                    PLAYER=1  
                    MESSAGE = "It's your turn!"
         
            elif hasWon(PLAYER, revealedBoxes):
	        currentBoard, revealedBoxes = gameOverScreen(currentBoard, revealedBoxes, PLAYER, 1)
            elif playersTied(revealedBoxes):
	        PLAYER = 0
                currentBoard, revealedBoxes = gameOverScreen(currentBoard, revealedBoxes, PLAYER, 1)
	        PLAYER = random.choice([1,2])
    	        if PLAYER == 1:
		    MESSAGE = "It's your turn!"
                else:
		    MESSAGE = "It's the computer's turn!"
            DISPLAYSURF.fill(BGCOLOR)
            drawBoard(currentBoard, revealedBoxes, MESSAGE)
	    pygame.display.update()
            boxx = None
            boxy = None
        
  	for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP and PLAYER == 1: 
                mousex, mousey = event.pos
                mouseClicked = True
                boxx, boxy = getSpotClicked(currentBoard, mousex, mousey)
        if boxx == None and boxy == None:
	    if NEW_RECT.collidepoint(mousex,mousey):
		numOfPlayers = showStartScreen()
		return numOfPlayers
        elif boxx != None and boxy != None and PLAYER == 1:
	    if not revealedBoxes[boxx][boxy] and mouseClicked:	
                revealedBoxes[boxx][boxy] = PLAYER
                drawBoard(currentBoard, revealedBoxes, MESSAGE)
                pygame.display.update()
		    
            if not hasWon(PLAYER, revealedBoxes) and not playersTied(revealedBoxes):   
                if PLAYER == 1:
		    PLAYER=2		
		    MESSAGE = "It's the computer's turn!"
                elif PLAYER == 2:
                    PLAYER=1  
                    MESSAGE = "It's your turn!"
         
            elif hasWon(PLAYER, revealedBoxes):
	        currentBoard, revealedBoxes = gameOverScreen(currentBoard, revealedBoxes, PLAYER, 1)
            elif playersTied(revealedBoxes):
	        PLAYER = 0
                currentBoard, revealedBoxes = gameOverScreen(currentBoard, revealedBoxes, PLAYER, 1)
	        PLAYER = random.choice([1,2])
    	        if PLAYER == 1:
		    MESSAGE = "It's your turn!"
                else:
		    MESSAGE = "It's the computer's turn!"
            drawBoard(currentBoard, revealedBoxes, MESSAGE)                 
    

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    

def runTwoPlayerGame(currentBoard, revealedBoxes):

    PLAYER = random.choice([1,2])
    MESSAGE = "It's player %d's turn!"%(PLAYER)
    drawBoard(currentBoard, revealedBoxes, MESSAGE)
    pygame.display.update()
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        mousex = 0 
        mousey = 0
        drawBoard(currentBoard, revealedBoxes, MESSAGE)
        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP: #? What keyword replaces '???' here?
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getSpotClicked(currentBoard, mousex, mousey)
        if boxx == None and boxy == None:
	    if NEW_RECT.collidepoint(mousex,mousey):
		numOfPlayers = showStartScreen()
		return numOfPlayers
        elif boxx != None and boxy != None:
	    if not revealedBoxes[boxx][boxy] and mouseClicked:	
                revealedBoxes[boxx][boxy] = PLAYER
                drawBoard(currentBoard, revealedBoxes, MESSAGE)
                pygame.display.update()
		    
         	if not hasWon(PLAYER, revealedBoxes) and not playersTied(revealedBoxes):   
		    if PLAYER == 1:
		        PLAYER=2
                    elif PLAYER == 2:
                        PLAYER=1  
                    MESSAGE = "It's player %d's turn!"%(PLAYER) 
		elif hasWon(PLAYER, revealedBoxes):
		    currentBoard, revealedBoxes = gameOverScreen(currentBoard, revealedBoxes, PLAYER, 2)
		elif playersTied(revealedBoxes):
		    PLAYER = 0
                    currentBoard, revealedBoxes = gameOverScreen(currentBoard, revealedBoxes, PLAYER, 2)
		    PLAYER = random.choice([1,2])
    	            MESSAGE = "It's player %d's turn!"%(PLAYER)
		    drawBoard(currentBoard, revealedBoxes, MESSAGE)
    		    pygame.display.update()
                 
    

        pygame.display.update()
        FPSCLOCK.tick(FPS)



def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes        

def showStartScreen():
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        drawTitle()
        PLAYERSURF, PLAYERRECT = makeText('2 Player', TEXTCOLOR, BGCOLOR, 320, 300)
   	DISPLAYSURF.blit(PLAYERSURF, PLAYERRECT)    
 
	VSSURF, VSRECT = makeText('vs Computer', TEXTCOLOR, BGCOLOR, 320, 400)
        DISPLAYSURF.blit(VSSURF, VSRECT)     
        
        checkForQuit()
        for event in pygame.event.get():
	    if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
	        if PLAYERRECT.collidepoint(mousex, mousey):
		    return 2
                elif VSRECT.collidepoint(mousex, mousey):
                    return 1

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawTitle():
    # create the Surface and Rect objects for some text.
    titleSurf = pygame.font.Font('freesansbold.ttf', 50).render("Tic Tac Toe", True, TILECOLOR, BGCOLOR)
    titleRect = titleSurf.get_rect()
    titleRect.center = (320, 100)
    DISPLAYSURF.blit(titleSurf, titleRect) 


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

def playersTied(revealed):
    for x in range(BOARDWIDTH):
	for y in range(BOARDHEIGHT):
	    if not revealed[x][y]:
		return False
    return True

def hasWon(player, revealed):
    global howWon
    if revealed[0][0] == player and revealed[0][1] == player and revealed[0][2] == player:
        howWon = 1
        return True
    elif revealed[1][0] == player and revealed[1][1] == player and revealed[1][2] == player:
	howWon = 2
	return True
    elif revealed[2][0] == player and revealed[2][1] == player and revealed[2][2] == player:
	howWon = 3
        return True
    elif revealed[0][0] == player and revealed[1][0] == player and revealed[2][0] == player:
	howWon = 4
	return True
    elif revealed[0][1] == player and revealed[1][1] == player and revealed[2][1] == player:
	howWon = 5
	return True
    elif revealed[0][2] == player and revealed[1][2] == player and revealed[2][2] == player:
	howWon = 6
	return True
    elif revealed[0][0] == player and revealed[1][1] == player and revealed[2][2] == player:
	howWon = 7
	return True
    elif revealed[2][0] == player and revealed[1][1] == player and revealed[0][2] == player:
	howWon = 8
	return True
    else:
        howWon = 0
        return False

def gameOverScreen(board, revealed, player, game):
    if player == 0:
	MESSAGE = "It's a tie!"
    else:
    	if game == 1:
            if player == 1:
		MESSAGE = "You win!"
	    else:
                MESSAGE = "The computer wins!"	
    	else:
            MESSAGE = "Player %d wins!"%(player)	
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR #? What color should go here?

    for i in range(13):
        color1, color2 = color2, color1 #? How can we swap the colors?
        DISPLAYSURF.fill(color1)
        drawBoard(board, revealed, MESSAGE)
        drawLine(howWon, player)
        pygame.display.update()
        pygame.time.wait(300)
    pygame.time.wait(1000)
    board = getStartingBoard()
    revealed = generateRevealedBoxesData(False)
    
    return board, revealed



def getStartingBoard():
    # Return a board data structure with tiles.
    counter = 1
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(counter)
            counter += BOARDWIDTH
        board.append(column)
        counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1

    return board



def getLeftTopOfTile(tileX, tileY):
    left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
    top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
    return (left, top)


def getSpotClicked(board, x, y):
    # from the x & y pixel coordinates, get the x & y board coordinates
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)


def drawTile(tilex, tiley, number, adjx=0, adjy=0):
    # draw a tile at board coordinates tilex and tiley, optionally a few
    # pixels over (determined by adjx and adjy)
    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))


def makeText(text, color, bgcolor, x, y):
    # create the Surface and Rect objects for some text.
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.center = (x, y)
    return (textSurf, textRect)


def drawBoard(board, revealed, message):
    #DISPLAYSURF.fill(BGCOLOR)
   
    textSurf, textRect = makeText(message, TEXTCOLOR, BGCOLOR, 320, 80)
    DISPLAYSURF.blit(textSurf, textRect)

    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                drawTile(tilex, tiley, board[tilex][tiley])
            if revealed[tilex][tiley] == 1 or revealed[tilex][tiley] == 2:
                drawIcon(revealed[tilex][tiley], tilex, tiley)

    left, top = getLeftTopOfTile(0, 0)
    width = BOARDWIDTH * TILESIZE
    height = BOARDHEIGHT * TILESIZE
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)

    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)

def drawIcon(player, x, y):
    quarter = int(TILESIZE * 0.25) # syntactic sugar
    half =    int(TILESIZE * 0.5)  # syntactic sugar
    left, top = getLeftTopOfTile(x, y) 
    if player == 1:
        pygame.draw.line(DISPLAYSURF, XCOLOR, (left+15, top+5), (left+TILESIZE-15,top+TILESIZE-5), 20)
        pygame.draw.line(DISPLAYSURF, XCOLOR, (left+15, top + TILESIZE-5), (left+TILESIZE-15, top+5), 20)
    elif player == 2:
        pygame.draw.circle(DISPLAYSURF, OCOLOR, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, TILECOLOR, (left + half, top + half), quarter )

def drawLine(howWon, player):
    x, y = getLeftTopOfTile(0,0)
    half = int(TILESIZE*0.5)

    if player == 1:
	LINECOLOR = XCOLOR
    else:
        LINECOLOR = OCOLOR

    if howWon == 1:
        pygame.draw.line(DISPLAYSURF, LINECOLOR, (x+half, y-10), (x+half,y+TILESIZE*BOARDHEIGHT+10),5)
    elif howWon == 2:
        pygame.draw.line(DISPLAYSURF, LINECOLOR, (x+TILESIZE+half, y-10), (x+TILESIZE+half,y+TILESIZE*BOARDHEIGHT+10),5)
    elif howWon == 3:
        pygame.draw.line(DISPLAYSURF, LINECOLOR, (x+2*TILESIZE+half, y-10), (x+2*TILESIZE+half,y+TILESIZE*BOARDHEIGHT+10),5)
    elif howWon == 4:
        pygame.draw.line(DISPLAYSURF, LINECOLOR, (x-10, y+half), (x+TILESIZE*BOARDWIDTH+10,y+half),5)
    elif howWon == 5:
        pygame.draw.line(DISPLAYSURF, LINECOLOR, (x-10, y+TILESIZE+half), (x+TILESIZE*BOARDWIDTH+10,y+TILESIZE+half),5)
    elif howWon == 6:
        pygame.draw.line(DISPLAYSURF, LINECOLOR, (x-10, y+2*TILESIZE+half), (x+TILESIZE*BOARDWIDTH+10,y+2*TILESIZE+half),5)
    elif howWon == 7:
        pygame.draw.line(DISPLAYSURF, LINECOLOR, (x-10, y-10), (x+TILESIZE*BOARDWIDTH+10,y+TILESIZE*BOARDHEIGHT+10),5)
    elif howWon == 8:
        pygame.draw.line(DISPLAYSURF, LINECOLOR, (x-10, y+TILESIZE*BOARDHEIGHT+10), (x+TILESIZE*BOARDWIDTH+10,y-10),5)



if __name__ == '__main__':
    main()
