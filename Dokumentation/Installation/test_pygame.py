import pygame
import sys
import time

pygame.init()
screen = pygame.display.set_mode((200,200))
pygame.draw.circle(screen, (0,0,255), (100,100), 30, 2)
pygame.display.update()
time.sleep(3)
