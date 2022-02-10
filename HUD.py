import pygame, sys, math

class HUD():
    def __init__(self, baseText, size, startPos=[0,0]):
        self.font = pygame.font.Font(None, 30)
        self.baseText = baseText
        self.size = size
        self.image = self.font.render(self.baseText + " 0", True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft = startPos)

    def update(self, score):
        text = self.baseText + str(score)
        self.image = self.font.render(self.baseText +str(int(score)), True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        width = self.size[0]
        height = self.size[1]

        if self.rect.right > width:
            self.rect.right = width - 10