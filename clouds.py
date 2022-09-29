import pygame
import random

class  Cloud(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.x = random.randrange(1,800)
        self.y = 850
        self.speed = random.uniform(0.2,0.5)
        self.screen = screen
        size = random.randrange(80,135)
        self.image = pygame.transform.scale(pygame.image.load("Art/Cloud"+str(random.randrange(1,3))+".png"),(size,size))

    def tick(self,speed):
        self.y -= self.speed * speed
        self.screen.blit(self.image,(self.x,self.y))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

