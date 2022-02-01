import pygame, sys, math, random
from ArrowTile import *

pygame.init()
    
clock = pygame.time.Clock();
    
size = [900, 700]
screen = pygame.display.set_mode(size)

arrows = [ArrowTile([0,5],[random.randint(10,590),-100])]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
            
    if random.randint(0,60)==0:
        arrows += [ArrowTile([0,5],[random.randint(10,590),-100])]

            
    for arrow in arrows:
        arrow.move()
        arrow.wallCollide(size)
        
        if arrow.living != True:
            arrows.remove(arrow)
        
    screen.fill((255, 128 , 64)) 
    for arrow in arrows:
        screen.blit(arrow.image, arrow.rect)
    pygame.display.flip()   
    clock.tick(60)
    print(clock.get_fps())
