import pygame, sys, math, random, os
from ArrowTile import *
from ArrowBox import *
from HUD import*
from LevelLoader import*
from Button import*
from ScoreLoader import*



pygame.init()
    
clock = pygame.time.Clock()
    
size = [900, 700]
screen = pygame.display.set_mode(size)


mode = "main menu"
backgroundSelected = "Backgrounds/Background 0.png"


while True:
#MAIN MENU
    if mode == "main menu":
        bgImage = pygame.image.load("Screens/Main Screen.png").convert()
        bgRect = bgImage.get_rect()
        pygame.mixer.music.load("Levels/Sounds/MB Rythm Smash Final FIX Main Menu Song - 2-16-22 9.30 AM.ogg")
        pygame.mixer.music.play()
        playButton = Button("play", [353, 543])
        quitButton = Button("quit", [710, 562])
        creditsButton = Button("credits", [59, 562])
    while mode == "main menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                playButton.hover(event.pos)
                quitButton.hover(event.pos)
                creditsButton.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:           #BUTTONS!!!
                playButton.clickDown(event.pos)
                quitButton.clickDown(event.pos)
                creditsButton.clickDown(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if playButton.clickUp(event.pos):
                    mode = "level select"
                if quitButton.clickUp(event.pos):
                    sys.exit()
                if creditsButton.clickUp(event.pos):
                    mode = "credits"

        mouse = pygame.mouse.get_pos()
        screen.fill((255, 128, 64))
        screen.blit(bgImage, bgRect)
        screen.blit(playButton.image, playButton.rect)
        screen.blit(quitButton.image, quitButton.rect)
        screen.blit(creditsButton.image, creditsButton.rect)
        pygame.display.flip()
        clock.tick(60)
        print()
        # print(clock.get_fps())

    score = HUD("Score: ", size, [0, 0])
    multiplier = HUD("Multiplier: ", size, [0, 30])
    streak = HUD("Streak: ", size, [0, 60])

    score2 = HUD("Score: ", size, [850, 0])
    multiplier2 = HUD("Multiplier: ", size, [850, 30])
    streak2 = HUD("Streak: ", size, [850, 60])

    points = 0
    multiply = 1
    continuous = 0

    points2 = 0
    multiply2 = 1
    continuous2 = 0

    player2 = False

    arrowBoxes = {"left": ArrowBox("left", [75, 550]),
                  "down": ArrowBox("down", [150, 550]),
                  "up": ArrowBox("up", [225, 550]),
                  "right": ArrowBox("right", [300, 550])}

    arrowBoxes2 = {"left": ArrowBox("left", [900-300, 550]),
                  "down": ArrowBox("down", [900-225, 550]),
                  "up": ArrowBox("up", [900-150, 550]),
                  "right": ArrowBox("right", [900-75, 550])}




#LEVEL SELECT
    if mode == "level select":
        LevelOneIcon = Button("LevelOne", [53, 60], "Levels/Icons/")
        playLevel = Button("playLevel", [441, 569])
        backgroundButton = Button("backgrounds", [450, 450])
        level = ""
        song = ""
    while mode == "level select":
        bgImage = pygame.image.load("Screens/Level Select.png").convert()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                LevelOneIcon.hover(event.pos)
                playLevel.hover(event.pos)
                backgroundButton.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:           #BUTTONS!!!
                LevelOneIcon.clickUp(event.pos)
                playLevel.clickUp(event.pos)
                backgroundButton.clickUp(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if LevelOneIcon.clickUp(event.pos):
                    level = "example"
                    song = "Levels/Sounds/Rythm smash final 150 Gm.ogg"
                    LevelOneIcon.reset()
                if playLevel.clickUp(event.pos):
                    if level and song != "":
                        mode = "game"
                    else:
                        playLevel.reset()
                if backgroundButton.clickUp(event.pos):
                    mode = "background select"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mode = "main menu"
        """
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if level and song != "":
                    if 464 <= mouse[0] <= 464 + 362 and 577 <= mouse[1] <= 577 + 72:
                        mode = "game"
"""

        mouse = pygame.mouse.get_pos()
        screen.blit(bgImage, bgRect)
        screen.blit(LevelOneIcon.image, LevelOneIcon.rect)
        screen.blit(playLevel.image, playLevel.rect)
        screen.blit(backgroundButton.image, backgroundButton.rect)
        pygame.display.flip()
        clock.tick(60)

### BG Select
    bgButtons = []
    xgap = 0
    ygap = 0
    if mode == "background select":
        for i in range(20):
            if i%5==0 and i!=0:
                ygap += 150
                xgap = 0

            bgButtons += [Button("bg" + str(i), [50+xgap, 40+ygap])]
            xgap += 160

        backButton = Button("back", [50, 600])

    while mode == "background select":
        bgImage = pygame.image.load("Backgrounds/Background 0.png").convert()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                backButton.hover(event.pos)
                for button in bgButtons:
                    button.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:  # BUTTONS!!!
                backButton.clickUp(event.pos)
                for button in bgButtons:
                    button.clickUp(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if backButton.clickUp(event.pos):
                    mode = "level select"
                for button in bgButtons:
                    if button.clickUp(event.pos):
                        i = button.baseText[2:]
                        backgroundSelected = "Backgrounds/Background " + str(i) + ".png"
                        print(button.baseText, i, backgroundSelected)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mode = "main menu"
        """
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if level and song != "":
                    if 464 <= mouse[0] <= 464 + 362 and 577 <= mouse[1] <= 577 + 72:
                        mode = "game"
"""

        mouse = pygame.mouse.get_pos()
        screen.blit(bgImage, bgRect)
        screen.blit(backButton.image, backButton.rect)
        for button in bgButtons:
            screen.blit(button.image, button.rect)
        pygame.display.flip()
        clock.tick(60)
#GAME
    if mode == "game":
        print(backgroundSelected)
        bgImage = pygame.image.load(backgroundSelected).convert()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        arrows = loadLevel(level)
        if player2:
            arrows2 = loadLevel(level, 2)

    while mode == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if not player2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mode = "main menu"
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
            if player2:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mode = "main menu"
                    if event.key == pygame.K_h:
                        arrowBoxes2["left"].active = True
                    elif event.key == pygame.K_LEFT:
                        arrowBoxes["left"].active = True
                    elif event.key == pygame.K_l:
                        arrowBoxes2["right"].active = True
                    elif event.key == pygame.K_RIGHT:
                        arrowBoxes["right"].active = True
                    elif event.key == pygame.K_k:
                        arrowBoxes2["up"].active = True
                    elif event.key == pygame.K_UP:
                        arrowBoxes["up"].active = True
                    elif event.key == pygame.K_j:
                        arrowBoxes2["down"].active = True
                    elif event.key == pygame.K_DOWN:
                        arrowBoxes["down"].active = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_h:
                        arrowBoxes2["left"].active = False
                    elif event.key == pygame.K_LEFT:
                        arrowBoxes["left"].active = False
                    elif event.key == pygame.K_l:
                        arrowBoxes2["right"].active = False
                    elif event.key == pygame.K_RIGHT:
                        arrowBoxes["right"].active = False
                    elif event.key == pygame.K_k:
                        arrowBoxes2["up"].active = False
                    elif event.key == pygame.K_UP:
                        arrowBoxes["up"].active = False
                    elif event.key == pygame.K_j:
                        arrowBoxes2["down"].active = False
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
        if player2:
            for arrow in arrows2:
                arrow.move()
                arrow.wallCollide(size)
                for box in arrowBoxes2.values():
                    if box.kind == arrow.kind and box.active:
                        if box.getDist(arrow) < 200:
                            points2 += 200 - (box.getDist(arrow) * int(multiply))
                            continuous2 += 1
                            arrow.living = False
                            if continuous2 == 10:
                                multiply2 += 1
                            if continuous2 == 25:
                                multiply2 += 1
                            if continuous2 == 40:
                                multiply2 += 1
                            if continuous2 == 70:
                                multiply2 += 1
                            if continuous2 == 100:
                                multiply2 = 10
                        elif box.getDist(arrow) > 200:
                            continuous2 = 0
                            multiply2 = 1

                        box.active = False

        score.update(points)
        multiplier.update(multiply)
        streak.update(continuous)

        score2.update(points2)
        multiplier2.update(multiply2)
        streak2.update(continuous2)

        for arrow in arrows:
            if not arrow.living:
                arrows.remove(arrow)
                if len(arrows) == 0:
                    mode = "end level"
                    pygame.mixer.music.load("Levels/Sounds/MB Rythm Smash Final FIX Main Menu Song - 2-16-22 9.30 AM.ogg")
                    pygame.mixer.music.play()
            if not arrow.available:
                continuous = 0
                multiply = 1
        if player2:
            for arrow in arrows2:
                if not arrow.living:
                    arrows2.remove(arrow)
                if not arrow.available:
                    continuous2 = 0
                    multiply = 1

        screen.blit(bgImage, bgRect)
        for box in arrowBoxes.values():
            screen.blit(box.image, box.rect)
        for arrow in arrows:
            screen.blit(arrow.image, arrow.rect)

        if player2:
            for box in arrowBoxes2.values():
                screen.blit(box.image, box.rect)
            for arrow in arrows2:
                screen.blit(arrow.image, arrow.rect)
            screen.blit(score2.image, score2.rect)
            screen.blit(multiplier2.image, multiplier2.rect)
            screen.blit(streak2.image, streak2.rect)

        screen.blit(score.image, score.rect)
        screen.blit(multiplier.image, multiplier.rect)
        screen.blit(streak.image, streak.rect)


        pygame.display.flip()
        clock.tick(60)
        print()
        #print(clock.get_fps())
#END LEVEL
    if mode == "end level":
        scores = loadScores(level)
        smallFont = pygame.font.SysFont('Calibri', 40)

        scores += [points, points2]
        scores.sort(reverse = True)
        scores = scores[0:10]

        saveScores(level, scores)

        scoreText = smallFont.render(str(points), True, (255, 255, 255))
        highText = smallFont.render(str(scores[0]), True, (255, 255, 255))
        scoretextRect = scoreText.get_rect(midtop=[435, 130])
        highTextRect = highText.get_rect(midtop=[435, 375])

        if player2:
            scoreText = smallFont.render(str(points), True, (255, 255, 255))
            highText = smallFont.render(str(scores[0]), True, (255, 255, 255))
            scoretextRect = scoreText.get_rect(midtop=[200, 130])
            highTextRect = highText.get_rect(midtop=[450, 475])

            scoreText2 = smallFont.render(str(points2), True, (255, 255, 255))
            scoretextRect2 = scoreText.get_rect(midtop=[680, 130])

        nextButton = Button("next", [650,600])
    while mode == "end level":
        bgImage = pygame.image.load("Screens/End Level Screen.png").convert()

        if player2:
            bgImage = pygame.image.load("Screens/2Player End Level Screen.png").convert()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mode = "main menu"
            if event.type == pygame.MOUSEMOTION:
                nextButton.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:           #BUTTONS!!!
                nextButton.clickDown(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if nextButton.clickUp(event.pos):
                    mode = "highscores"

        mouse = pygame.mouse.get_pos()
        screen.blit(bgImage, bgRect)
        screen.blit(scoreText, scoretextRect)
        screen.blit(highText, highTextRect)
        if player2:
            screen.blit(scoreText2, scoretextRect2)
        screen.blit(nextButton.image, nextButton.rect)
        pygame.display.flip()
        clock.tick(60)
#HIGHSCORES
    if mode == "highscores":
        levelselectButton = Button("levelselect", [50, 625])
        smallFont = pygame.font.SysFont('Consolas', 38)
        renderList = []
        y = 135
        yChange = 45
        for i, score in enumerate(scores):
            if i+1 < 10:
                highText = smallFont.render(str(i+1)+".  "+str(score), True, (255, 255, 255))
            else:
                highText = smallFont.render(str(i + 1) + ". " + str(score), True, (255, 255, 255))
            highTextRect = highText.get_rect(topleft=[500, y])
            y+= yChange
            listItem = [highText, highTextRect]
            renderList += [listItem]
    while mode == "highscores":
        bgImage = pygame.image.load("Screens/Highscores.png").convert()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mode = "main menu"
            if event.type == pygame.MOUSEMOTION:
                levelselectButton.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:  # BUTTONS!!!
                levelselectButton.clickDown(event.pos)

            if event.type == pygame.MOUSEBUTTONUP:
                if levelselectButton.clickUp(event.pos):
                    mode = "level select"

        mouse = pygame.mouse.get_pos()
        screen.blit(bgImage, bgRect)
        for item in renderList:
            screen.blit(item[0], item[1])
        screen.blit(levelselectButton.image, levelselectButton.rect)
        pygame.display.flip()
        clock.tick(60)
### CREDITS
    if mode == "credits":
        mainmenuButton = Button("main menu", [59, 562])
        bgImage = pygame.image.load("Screens/Credits.png").convert()
    while mode == "credits":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mainmenuButton.hover(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:  # BUTTONS!!!
                mainmenuButton.clickDown(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if mainmenuButton.clickUp(event.pos):
                    mode = "main menu"

        mouse = pygame.mouse.get_pos()
        screen.blit(bgImage, bgRect)
        screen.blit(mainmenuButton.image, mainmenuButton.rect)
        pygame.display.flip()
        clock.tick(60)

