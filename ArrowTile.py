import pygame, sys, math

class ArrowTile():
    def __init__(self, kind, speed = [0,10], startPos=[0,0]):
        self.kind = kind
        self.image = pygame.image.load("Arrows/ArrowTiles/Images/" + self.kind + "Arrow.png")
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2
        self.rect = self.rect.move(startPos)
        self.living = True
        self.available = True


    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if self.rect.bottom > height:
            self.living = False
            self.available = False
        
            
    def ballCollide(self, other) :
        if self.rect.right > other.rect.left:
            if self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top:
                    if self.rect.top < other.rect.bottom:
                        if self.getDist(other) < self.rad + other.rad:
                            self.speedx = -self.speedx
                            self.speedy = -self.speedy
                            
        

    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 =  other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
