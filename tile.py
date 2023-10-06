import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        img = pygame.image.load('../Zelda_Pygame/pic/rock.png')
        self.image = pygame.transform.scale(img, (100,100)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)