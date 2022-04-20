import pygame, sys, math, random
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
backgroundSelected = "Backgrounds/Background.png"


while True:
#MAIN MENU
    if mode == "main menu":
        bgImage = pygame.image.load("Screens/Main Screen.png")
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

    points = 0
    multiply = 1
    continuous = 0

    arrowBoxes = {"left": ArrowBox("left", [75, 550]),
                  "down": ArrowBox("down", [150, 550]),
                  "up": ArrowBox("up", [225, 550]),
                  "right": ArrowBox("right", [300, 550])}



#LEVEL SELECT
    if mode == "level select":
        LevelOneIcon = Button("LevelOne", [53, 60], "Levels/Icons/")
        playLevel = Button("playLevel", [441, 569])
        backgroundButton = Button("backgrounds", [450, 450])
        level = ""
        song = ""
    while mode == "level select":
        bgImage = pygame.image.load("Screens/Level Select.png")

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
        bgImage = pygame.image.load("Backgrounds/Background.png")

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
        bgImage = pygame.image.load(backgroundSelected)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        arrows = loadLevel(level)

    while mode == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
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
                    mode = "end level"
                    pygame.mixer.music.load("Levels/Sounds/MB Rythm Smash Final FIX Main Menu Song - 2-16-22 9.30 AM.ogg")
                    pygame.mixer.music.play()
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
#END LEVEL
    if mode == "end level":
        scores = loadScores(level)
        smallFont = pygame.font.SysFont('Calibri', 40)

        scores += [points]
        scores.sort(reverse = True)
        scores = scores[0:10]

        saveScores(level, scores)

        scoreText = smallFont.render(str(points), True, (255, 255, 255))
        highText = smallFont.render(str(scores[0]), True, (255, 255, 255))
        scoretextRect = scoreText.get_rect(midtop=[435, 130])
        highTextRect = highText.get_rect(midtop=[435, 375])
    while mode == "end level":
        bgImage = pygame.image.load("Screens/End Level Screen.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mode = "main menu"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 684 <= mouse[0] <= 684 + 150 and 588 <= mouse[1] <= 588 + 48:
                    mode = "highscores"

        mouse = pygame.mouse.get_pos()
        screen.blit(bgImage, bgRect)
        screen.blit(scoreText, scoretextRect)
        screen.blit(highText, highTextRect)
        pygame.display.flip()
        clock.tick(60)
#HIGHSCORES
    if mode == "highscores":
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
        bgImage = pygame.image.load("Screens/Highscores.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mode = "main menu"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 34 <= mouse[0] <= 34 + 182 and 588 <= mouse[1] <= 616 + 51:
                    mode = "level select"

        mouse = pygame.mouse.get_pos()
        screen.blit(bgImage, bgRect)
        for item in renderList:
            screen.blit(item[0], item[1])
        pygame.display.flip()
        clock.tick(60)
### CREDITS
    if mode == "credits":
        mainmenuButton = Button("main menu", [59, 562])
        bgImage = pygame.image.load("Screens/Credits.png")
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
