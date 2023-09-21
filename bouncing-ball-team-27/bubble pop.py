import pygame
import constants
import bubble_arrow


def addBubbleToTop(bubbleArray, bubble):
    posx = bubble.rect.centerx
    leftSidex = posx - bubbleradius
    columnDivision = math.modf(float(leftSidex) / float(bubblediameter))
    column = int(columnDivision[1])
    if columnDivision[0] < 0.5:# toucing the wall condition
        bubbleArray[0][column] = copy.copy(bubble)
    else:
        column += 1
        bubbleArray[0][column] = copy.copy(bubble)
    row = 0
    return row, column
# Conditions to pop the bubbles
def popBubbles(bubbleArray, row, column, color, deleteList):
    if row < 0 or column < 0 or row > (len(bubbleArray)-1) or column > (len(bubbleArray[0])-1):
        return
    elif bubbleArray[row][column] == BLANK:
        return
    elif bubbleArray[row][column].color != color:
        return
    for bubble in deleteList:
        if bubbleArray[bubble[0]][bubble[1]] == bubbleArray[row][column]:
            return
    deleteList.append((row, column))
    if row == 0:
        popBubbles(bubbleArray, row,     column - 1, color, deleteList)
        popBubbles(bubbleArray, row,     column + 1, color, deleteList)
        popBubbles(bubbleArray, row + 1, column,     color, deleteList)
        popBubbles(bubbleArray, row + 1, column - 1, color, deleteList)
    elif row % 2 == 0:        
        popBubbles(bubbleArray, row + 1, column,         color, deleteList)
        popBubbles(bubbleArray, row + 1, column - 1,     color, deleteList)
        popBubbles(bubbleArray, row - 1, column,         color, deleteList)
        popBubbles(bubbleArray, row - 1, column - 1,     color, deleteList)
        popBubbles(bubbleArray, row,     column + 1,     color, deleteList)
        popBubbles(bubbleArray, row,     column - 1,     color, deleteList)
    else:
        popBubbles(bubbleArray, row - 1, column,     color, deleteList)
        popBubbles(bubbleArray, row - 1, column + 1, color, deleteList)
        popBubbles(bubbleArray, row + 1, column,     color, deleteList)
        popBubbles(bubbleArray, row + 1, column + 1, color, deleteList)
        popBubbles(bubbleArray, row,     column + 1, color, deleteList)
        popBubbles(bubbleArray, row,     column - 1, color, deleteList)
#
def drawBubbleArray(array):
    for row in range(arrayheight):
        for column in range(len(array[row])):
            if array[row][column] != BLANK:
                array[row][column].draw()                    
#displaying the board
def makeDisplay():
    DISPLAYSURF = pygame.display.set_mode((width, height))
    DISPLAYRECT = DISPLAYSURF.get_rect()
    DISPLAYSURF.fill(bgcolor)
    DISPLAYSURF.convert()
    pygame.display.update()
    return DISPLAYSURF, DISPLAYRECT
def terminate():
    pygame.quit()
    sys.exit()
#  next bubble
def coverNextBubble():
    whiteRect = pygame.Rect(0, 0, bubblediameter, bubblediameter)
    whiteRect.bottom = height
    whiteRect.right = width
    pygame.draw.rect(DISPLAYSURF, bgcolor, whiteRect)