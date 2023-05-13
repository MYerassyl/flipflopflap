import pygame
import assets as ast
import settings as set

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ast.background_base
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Move Ground
        self.rect.x -= set.scroll_speed
        if self.rect.x <= -set.win_width:
            self.kill()
