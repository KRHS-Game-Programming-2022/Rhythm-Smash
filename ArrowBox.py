import pygame, sys, math


class ArrowBox():
    def __init__(self, kind, startPos=[0, 0]):
        self.kind = kind
        self.image = pygame.image.load("Arrows/ArrowBox/Images/" + self.kind + "ArrowBox.png").convert_alpha()
        self.rect = self.image.get_rect(center=startPos)
        self.rad = (self.rect.height / 2 + self.rect.width / 2) / 2
        #self.rect = self.rect.move(startPos)

        self.living = True

        self.active = False


    def getDist(self, other):
        y1 = self.rect.centery
        y2 = other.rect.centery
        return abs(y2-y1)
