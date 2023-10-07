import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        img = pygame.image.load('../Zelda_Pygame/pic/player.png')
        self.image = pygame.transform.scale(img, (50,50)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)