import pygame
import math, sys, os, copy, time, random
import pygame.gfxdraw
from pygame.locals import *
## Constants, yo ##
fps    = 120   #  frame per second
width  = 600   
height = 400
bubbleradius = 20
bubblediameter  = bubbleradius * 2
layers = 6
bubbleadjust = 5 # distance between two layers
startX = width / 2
startY = height - 30
arraywidth = 16
arrayheight = 14
right = 'right'
left  = 'left'
BLANK = '.'
## COLORS ##
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,  0,  255)
BLACK    = (  0,   0,   0)
GRAY     = (100, 100, 100)
bgcolor    = WHITE
COLORLIST = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, GRAY]