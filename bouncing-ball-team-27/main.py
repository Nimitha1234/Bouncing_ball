import pygame
import sys
import constants
import bubble_pop
import 

def main():
    global FPSCLOCK, DISPLAYSURF, DISPLAYRECT, MAINFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock() 
    pygame.display.set_caption('Puzzle Bobble')
    MAINFONT = pygame.font.SysFont('Helvetica', 20)
    DISPLAYSURF, DISPLAYRECT = makeDisplay() # displaying the name
    while True:
        score, winorlose = runGame() # running the game
        endScreen(score, winorlose) # ending screen
def runGame():
    musicList =['bgmusic.ogg', 'Utopian_Theme.ogg', 'Goofy_Theme.ogg'] # background music
    pygame.mixer.music.load(musicList[0]) # command to play music 
    pygame.mixer.music.play()
    track = 0
    gameColorList = copy.deepcopy(COLORLIST) # colours
    direction = None # starting direction
    launchBubble = False 
    newBubble = None
    arrow = Arrow()
    bubbleArray = makeBlankBoard() # forming a list
    setBubbles(bubbleArray, gameColorList)  # setting the bubbles
    nextBubble = Bubble(gameColorList[0])  # firing bubble
    nextBubble.rect.right = width - 5 # showing it at the right corner
    nextBubble.rect.bottom = height - 5 
    score = Score() # initialising score class
    while True:
        DISPLAYSURF.fill(bgcolor) 
        for event in pygame.event.get(): # to run the game the event should be start in the pygame
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN: 
                if (event.key == K_LEFT): # left key to the left direction
                    direction = left
                elif (event.key == K_RIGHT): # right key to the right direction
                    direction = right                    
            elif event.type == KEYUP: # no movement
                direction = None
                if event.key == K_SPACE: # lanch
                    launchBubble = True
                elif event.key == K_ESCAPE: # to stop the game
                    terminate()
        if launchBubble == True: # lanching bubble
            if newBubble == None:
                newBubble = Bubble(nextBubble.color) # any color bubble
                newBubble.angle = arrow.angle # changing the arrow direction
            newBubble.update() # updating the next bubble
            newBubble.draw() 
            if newBubble.rect.right >= width - 5: # firing angle
                newBubble.angle = 180 - newBubble.angle 
            elif newBubble.rect.left <= 5:
                newBubble.angle = 180 - newBubble.angle
            launchBubble, newBubble, score = stopBubble(bubbleArray, newBubble, launchBubble, score) # strucking the launch bubble
            finalBubbleList = [] # for total game 
            for row in range(len(bubbleArray)):
                for column in range(len(bubbleArray[0])):
                    if bubbleArray[row][column] != BLANK:
                        finalBubbleList.append(bubbleArray[row][column]) # adding the firing bubble at the bubble 
                        if bubbleArray[row][column].rect.bottom > (height - arrow.rect.height - 10): # ending line condition
                            return score.total, 'lose'            
            if len(finalBubbleList) < 1: # game completed
                return score.total, 'win'
            gameColorList = updateColorList(bubbleArray) # to the next game
            random.shuffle(gameColorList) # to change the colour to next game
            if launchBubble == False: # if the bubble is not launched
                nextBubble = Bubble(gameColorList[0]) # no change in the color
                nextBubble.rect.right = width - 5
                nextBubble.rect.bottom = height - 5
        nextBubble.draw() 
        if launchBubble == True:
            coverNextBubble()        
        arrow.update(direction) # updating the arrow direction
        arrow.draw() 
        setArrayPos(bubbleArray) # updating the bubble array
        drawBubbleArray(bubbleArray)
        score.draw() # updating the score
        if pygame.mixer.music.get_busy() == False:
            if track == len(musicList) - 1:
                track = 0
            else:
                track += 1
            pygame.mixer.music.load(musicList[track])
            pygame.mixer.music.play()
        pygame.display.update()
        FPSCLOCK.tick(fps)
def makeBlankBoard(): # creating the balnk board
    array = []    
    for row in range(arrayheight):
        column = []
        for i in range(arraywidth):
            column.append(BLANK)
        array.append(column)
    return array
def setBubbles(array, gameColorList): # creating the  bubble layers
    for row in range(layers): 
        for column in range(len(array[row])):
            random.shuffle(gameColorList)
            newBubble = Bubble(gameColorList[0], row, column)
            array[row][column] = newBubble             
    setArrayPos(array)
def setArrayPos(array): # arranging the bubbles in the layers
    for row in range(arrayheight):
        for column in range(len(array[row])):
            if array[row][column] != BLANK:
                array[row][column].rect.x = (bubblediameter * column) + 5 # distance between the bubbles
                array[row][column].rect.y = (bubblediameter * row) + 5
    for row in range(1, arrayheight, 2):  # arranging the layers along the x axis
        for column in range(len(array[row])):
            if array[row][column] != BLANK:
                array[row][column].rect.x += bubbleradius 
    for row in range(1, arrayheight):
        for column in range(len(array[row])):
            if array[row][column] != BLANK:
                array[row][column].rect.y -= (bubbleadjust * row) # gap between the layers along y axis
    deleteExtraBubbles(array)
def deleteExtraBubbles(array): # deleting the extra bubble
    for row in range(arrayheight): 
        for column in range(len(array[row])):
            if array[row][column] != BLANK:
                if array[row][column].rect.right > width:
                    array[row][column] = BLANK
def updateColorList(bubbleArray):
    newColorList = [] 
    for row in range(len(bubbleArray)):
        for column in range(len(bubbleArray[0])):
            if bubbleArray[row][column] != BLANK: # adding the color to the new list
                newColorList.append(bubbleArray[row][column].color)
    colorSet = set(newColorList) # updated color list
    if len(colorSet) < 1:
        colorList = [] # no colur in the color set
        colorList.append(WHITE) # adding white if it is blank
        return colorList
    else:
        return list(colorSet)