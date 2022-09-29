import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.y = 400
        self.x = 400
        self.xVel = 0
        self.screen = screen
        self.image = pygame.image.load("Art/Tree1.png")
    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.xVel< 2:
                self.xVel +=0.01
        if keys[pygame.K_LEFT]:
            if self.xVel > -2:
                self.xVel -= 0.01
        self.x += self.xVel


        self.screen.blit(pygame.transform.rotate(self.image, self.xVel*-10), (self.x,self.y))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y