import pygame
import random
import time
from clouds import Cloud
from tree import Tree
from player import Player

#Set Up Screen
background_color = (135, 206, 235)
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Falling in Fall')
screen.fill(background_color)

#Create Var
cloudTime = 0
treeTime = 0
speed = 1
sAlpha = 0

#Create Insances
clouds = pygame.sprite.Group()
trees = []
player = Player(screen)




running = True

while running:



    #Clear Screen
    screen.fill(background_color)
    #Run Ticks
    for tree in trees:
        tree.tick(speed)
        if tree.y <= -200:
            trees.remove(tree)
            del tree
    for cloud in clouds:
        cloud.tick(speed)
        if cloud.y <= -135:
            clouds.remove(cloud)
            del cloud
    player.tick()
    if pygame.sprite.spritecollideany(player, clouds) != None:
        s = pygame.Surface((800, 800))
        sAlpha+=10
        if sAlpha > 250:
            sAlpha = 250
        s.set_alpha(sAlpha)
        s.fill((255, 255, 255))
        screen.blit(s, (0, 0))
    speed = abs(player.xVel)+1


    #Run Timers
    cloudTime+=1*speed
    treeTime+=1*speed



    #Check Timers
    if cloudTime >= 240:
        clouds.add(Cloud(screen))
        cloudTime = 0
    if treeTime >= 200:
        trees.append(Tree(screen))
        treeTime = 0

    #Check Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    running = False

    #Update Screen
    pygame.display.flip()
