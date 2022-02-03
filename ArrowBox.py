import pygame, sys, math


class ArrowBox():
    def __init__(self, kind, startPos=[0, 0]):
        self.kind = kind
        self.image = pygame.image.load("Arrows/ArrowTiles/Images/"+ self.kind + "Arrow.png")
        self.rect = self.image.get_rect()
        self.rad = (self.rect.height / 2 + self.rect.width / 2) / 2
        self.rect = self.rect.move(startPos)

        self.living = True


    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)