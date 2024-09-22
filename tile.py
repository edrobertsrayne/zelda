import pygame
from settings import TILESIZE


class Tile(pygame.sprite.Sprite):
    def __init__(
        self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))
    ) -> None:
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if self.sprite_type == "object":
            self.rect: pygame.Rect = self.image.get_rect(
                topleft=(pos[0], pos[1] - TILESIZE)
            )
        else:
            self.rect: pygame.Rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
