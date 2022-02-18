import pygame, sys, math, random
from ArrowTile import *
from ArrowBox import *
from HUD import*
from LevelLoader import*



pygame.init()
    
clock = pygame.time.Clock()
    
size = [900, 700]
screen = pygame.display.set_mode(size)


mode = "main menu"

while True:
    bgImage = pygame.image.load("Screens/Main Screen.png")
    bgRect = bgImage.get_rect()


    while mode == "main menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "game"
                    bgImage = pygame.image.load("Screens/Blank Background.png")

        screen.fill((255, 128, 64))
        screen.blit(bgImage, bgRect)

        pygame.display.flip()
        clock.tick(60)
        print()
        # print(clock.get_fps())

    score = HUD("Score: ", size, [0, 0])
    multiplier = HUD("Multiplier: ", size, [0, 30])
    streak = HUD("Streak: ", size, [0, 60])

    points = 0
    multiply = 1
    continuous = 0

    arrows = loadLevel("example.lvl")
    arrowBoxes = {"left": ArrowBox("left", [75, 550]),
                  "down": ArrowBox("down", [150, 550]),
                  "up": ArrowBox("up", [225, 550]),
                  "right": ArrowBox("right", [300, 550])}

    while mode == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_h:
                    arrowBoxes["left"].active = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_l:
                    arrowBoxes["right"].active = True
                elif event.key == pygame.K_UP or event.key == pygame.K_k:
                    arrowBoxes["up"].active = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_j:
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
        """
        if random.randint(0, 60) == 0:
            kinds = ["left", "down", "up", "right"]
            val = random.randint(0,3)
            arrows += [ArrowTile(kinds[int(val)], [0,5], [int(val)*75+75, -100])]
            #print(len(arrows))
        """

        for arrow in arrows:
            arrow.move()
            arrow.wallCollide(size)
            for box in arrowBoxes.values():
                if box.kind == arrow.kind and box.active:
                    if box.getDist(arrow) < 200:
                        points += 200-(box.getDist(arrow)*int(multiply))
                        continuous += 1
                        arrow.living = False
                        if continuous == 10:
                            multiply += 1
                        if continuous == 25:
                            multiply += 1
                        if continuous == 40:
                            multiply += 1
                        if continuous == 70:
                            multiply += 1
                        if continuous == 100:
                            multiply = 10
                    elif box.getDist(arrow) > 200:
                        continuous = 0
                        multiply = 1

                    box.active = False

        score.update(points)
        multiplier.update(multiply)
        streak.update(continuous)

        for arrow in arrows:
            if not arrow.living:
                arrows.remove(arrow)
                if len(arrows) == 0:
                    mode = "scores"
            if not arrow.available:
                continuous = 0
                multiply = 1

        screen.blit(bgImage, bgRect)
        for box in arrowBoxes.values():
            screen.blit(box.image, box.rect)
        for arrow in arrows:
            screen.blit(arrow.image, arrow.rect)
        screen.blit(score.image, score.rect)
        screen.blit(multiplier.image, multiplier.rect)
        screen.blit(streak.image, streak.rect)


        pygame.display.flip()
        clock.tick(60)
        print()
        #print(clock.get_fps())

    score = HUD("Score: ", size, [450, 350])
    score.update(points)
    while mode == "scores":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "main menu"

        screen.fill((64, 64, 64))
        screen.blit(score.image, score.rect)
        pygame.display.flip()
        clock.tick(60)