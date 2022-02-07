import pygame, sys, math, random
from ArrowTile import *
from ArrowBox import *

pygame.init()
    
clock = pygame.time.Clock()
    
size = [900, 700]
screen = pygame.display.set_mode(size)
score = 0

arrows = []
arrowBoxes = {"left": ArrowBox("left", [75, 550]),
              "up": ArrowBox("up", [150, 550]),
              "down": ArrowBox("down", [225, 550]),
              "right": ArrowBox("right", [300, 550])}

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                arrowBoxes["left"].active = True
            elif event.key == pygame.K_RIGHT:
                arrowBoxes["right"].active = True
            elif event.key == pygame.K_UP:
                arrowBoxes["up"].active = True
            elif event.key == pygame.K_DOWN:
                arrowBoxes["down"].active = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                arrowBoxes["left"].active = False
            elif event.key == pygame.K_RIGHT:
                arrowBoxes["right"].active = False
            elif event.key == pygame.K_UP:
                arrowBoxes["up"].active = False
            elif event.key == pygame.K_DOWN:
                arrowBoxes["down"].active = False

    if random.randint(0, 60) == 0:
        kinds = ["left", "down", "up", "right"]
        val = random.randint(0,3)
        arrows += [ArrowTile(kinds[int(val)], [0,5], [int(val)*75+75, -100])]
        #print(len(arrows))

    for arrow in arrows:
        arrow.move()
        arrow.wallCollide(size)
        for box in arrowBoxes.values():
            if box.kind == arrow.kind and box.active:
                if box.getDist(arrow) < 200:
                    score += box.getDist(arrow)
                    arrow.living = False
                box.active = False


    for arrow in arrows:
        if not arrow.living:
            arrows.remove(arrow)
        
    screen.fill((255, 128, 64))
    for box in arrowBoxes.values():
        screen.blit(box.image, box.rect)
    for arrow in arrows:
        screen.blit(arrow.image, arrow.rect)


    pygame.display.flip()   
    clock.tick(60)
    print()
    #print(clock.get_fps())
