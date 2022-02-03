import pygame, sys, math, random
from ArrowTile import *
from ArrowBox import *

pygame.init()
    
clock = pygame.time.Clock()
    
size = [900, 700]
screen = pygame.display.set_mode(size)

arrows = []
arrowBoxes = [ArrowBox([100, 550]), ArrowBox([200, 550]), ArrowBox([300, 550]), ArrowBox([400, 550])]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    if random.randint(0,60)==0:
        arrows += [ArrowTile([0,5],[random.randint(1,4)*100,-100])]

            
    for arrow in arrows:
        arrow.move()
        arrow.wallCollide(size)
        
        if arrow.living != True:
            arrows.remove(arrow)
        
    screen.fill((255, 128 , 64))
    for box in arrowBoxes:
        screen.blit(box.image, box.rect)
    for arrow in arrows:
        screen.blit(arrow.image, arrow.rect)

    pygame.display.flip()   
    clock.tick(60)
    print()
    #print(clock.get_fps())
