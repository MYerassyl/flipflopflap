import pygame

import assets as ast
import settings as set
class Bird(pygame.sprite.Sprite):
    def __init__(self, ch):
        self.ch = ch
        pygame.sprite.Sprite.__init__(self)
        self.image = ast.birdie_skins[ch][0]
        self.rect = self.image.get_rect()
        self.rect.center = set.bird_start_position
        self.image_index = 0
        self.vel = 0
        self.flap = False
        self.alive = True

    def update(self, user_input):
        # Animate Bird
        if self.alive:
            self.image_index += 1
        if self.image_index >= 30:
            self.image_index = 0
        self.image = ast.birdie_skins[self.ch][self.image_index // 10]

        # Gravity and Flap

        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect.y < 480:
            self.rect.y += int(self.vel)
        if self.vel == 0:
            self.flap = False

        # Rotate Bird
        self.image = pygame.transform.rotate(self.image, self.vel * -7)
        # User Input
        if user_input[pygame.K_SPACE] and not self.flap and self.rect.y > 0 and self.alive:
            hit = True
            if hit:
                music = pygame.mixer.Sound("flappy-bird-assets-master/audio/wing.wav")
                music.play(loops = 0)
                hit = False
            self.flap = True
            self.vel = -7
