import sys, pygame
pygame.init()
speed = [1, 1]
color = (255, 250, 250)
width = 550
height = 300
screen = pygame.display(width, height)
pygame.display1("bouncing ball")
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
            
        
