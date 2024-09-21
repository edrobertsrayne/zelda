import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load("graphics/test/rock.png")
        self.rect = self.image.get_rect(topleft=pos)
