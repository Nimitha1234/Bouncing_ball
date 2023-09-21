import constants
import pygame
import math
import pygame.gfxdraw
from constants import *
from pygame.locals import *

class Bubble(pygame.sprite.Sprite):
    def _init_(self, color, row=0, column=0):
        pygame.sprite.Sprite._init_(self)
        self.rect = pygame.Rect(0, 0, 30, 30)
        self.rect.centerx = startX
        self.rect.centery = startY
        self.speed = 10  # speed of the firing ball 
        self.color = color
        self.radius = bubbleradius
        self.angle = 0
        self.row = row # no.of rows
        self.column = column # no.of colums
    def update(self):
        if self.angle == 90:
            xmove = 0
            ymove = self.speed * -1 # making the speed 0
        elif self.angle < 90:
            xmove = self.xcalculate(self.angle) # calculating sin value
            ymove = self.ycalculate(self.angle) #calculating cos value
        elif self.angle > 90:
            xmove = self.xcalculate(180 - self.angle) * -1 # as it is in 2nd quadrant changing the sign
            ymove = self.ycalculate(180 - self.angle)     # calculating the cos values
        self.rect.x += xmove # change in x axis
        self.rect.y += ymove #change in y axis
    def draw(self):
        pygame.gfxdraw.filled_circle(DISPLAYSURF, self.rect.centerx, self.rect.centery, self.radius, self.color) #drawing a circle
        pygame.gfxdraw.aacircle(DISPLAYSURF, self.rect.centerx, self.rect.centery, self.radius, GRAY) #Border color
    def xcalculate(self, angle):
        radians = math.radians(angle)    # coverting it into radians
        xmove = math.cos(radians)*(self.speed) # giving the direction and value
        return xmove
    def ycalculate(self, angle):
        radians = math.radians(angle)    
        ymove = math.sin(radians)*(self.speed) * -1  # only upwards so -1
        return ymove
class Arrow(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.angle = 90
        arrowImage = pygame.image.load('Arrow.png') #image of arrow
        arrowImage.convert_alpha() # to get image on the screen
        arrowRect = arrowImage.get_rect() # in the tectangle
        self.image = arrowImage
        self.transformImage = self.image
        self.rect = arrowRect # placing it in the rectangle
        self.rect.centerx = startX  # placing at the center
        self.rect.centery = startY
    def update(self, direction):    
        if direction == left and self.angle < 180:
            self.angle += 1 #changing angle  of the arrow
        elif direction == right and self.angle > 0:        
            self.angle -= 1 # aas they are in oposite directions we decrese
        self.transformImage = pygame.transform.rotate(self.image, self.angle) # updating the arrow position
        self.rect = self.transformImage.get_rect() 
        self.rect.centerx = startX # at the center
        self.rect.centery = startY    
    def draw(self):
        DISPLAYSURF.blit(self.transformImage, self.rect) # flag used to draw the arrow at current location