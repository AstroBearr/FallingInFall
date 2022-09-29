import pygame
import random

class Tree():
    def __init__(self,screen):
        self.tree1 = pygame.transform.scale(pygame.image.load("Art/Tree1.png"),(100,200))
        self.tree2 = pygame.transform.scale(pygame.image.load("Art/Tree2.png"),(100,200))
        self.y = 850
        if random.randrange(1,3) == 1:
            self.currentTree = self.tree1
        else:
            self.currentTree = self.tree2
        self.screen = screen
    def tick(self,speed):
        self.y -= 0.7 * speed
        self.screen.blit(self.currentTree, (0, self.y))