import pygame
from tile import Tile
from player import Player
from settings import TILESIZE, WORLD_MAP


class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == "x":
                    Tile((x, y), [self.visible_sprites])
                elif col == "p":
                    Player((x, y), [self.visible_sprites])

    def run(self):
        self.visible_sprites.draw(self.display_surface)
