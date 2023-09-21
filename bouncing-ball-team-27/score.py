import pygame
import constants
from constants import *


class Score(object):
    def _init_(self):
        self.total = 0
        self.font = pygame.font.SysFont('Helvetica', 15)
        self.render = self.font.render('Score: ' + str(self.total), True, BLACK, WHITE) # score is projected 
        self.rect = self.render.get_rect() # getting rectangle
        self.rect.left = 5 #at the left end
        self.rect.bottom = height - 5      #  height of the rectangle  
    def update(self, deleteList):
        self.total += ((len(deleteList)) * 10) # no.of bubble is deletlist number
        self.render = self.font.render('Score: ' + str(self.total), True, BLACK, WHITE) # projecting the score
    def draw(self):
        DISPLAYSURF.blit(self.render, self.rect) # drawing at it curent loction