import pygame
import assets as ast
import settings as set

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image, pipe_type):
        pygame.sprite.Sprite.__init__(self)
        if pipe_type != "bottom":
            self.fl = pygame.transform.flip(image, False, True)
        else:
            self.fl = image
        self.image = self.fl
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.enter, self.exit, self.passed = False, False, False
        self.pipe_type = pipe_type

    def update(self):
        # Move Pipe
        self.rect.x -= set.scroll_speed
        if self.rect.x <= -set.win_width:
            self.kill()

        # Score
        if self.pipe_type == 'bottom':
            if set.bird_start_position[0] > self.rect.topleft[0] and not self.passed:
                self.enter = True
            if set.bird_start_position[0] > self.rect.topright[0] and not self.passed:
                self.exit = True
            if self.enter and self.exit and not self.passed:
                self.passed = True
                music = pygame.mixer.Sound("flappy-bird-assets-master/audio/point.wav")
                music.play(loops = 0)
                set.score += 1
