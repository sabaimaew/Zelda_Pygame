import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def ___init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../pic/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)