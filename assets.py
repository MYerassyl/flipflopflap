import pygame

# Images

birdie_skins = [[pygame.image.load("flappy-bird-assets-master/sprites/redbird-downflap.png"),
                 pygame.image.load("flappy-bird-assets-master/sprites/redbird-midflap.png"),
                 pygame.image.load("flappy-bird-assets-master/sprites/redbird-upflap.png")],
                [ pygame.image.load("flappy-bird-assets-master/sprites/bluebird-downflap.png"),
                  pygame.image.load("flappy-bird-assets-master/sprites/bluebird-midflap.png"),
                  pygame.image.load("flappy-bird-assets-master/sprites/bluebird-upflap.png")],
                [ pygame.image.load("flappy-bird-assets-master/sprites/yellowbird-downflap.png"),
                  pygame.image.load("flappy-bird-assets-master/sprites/yellowbird-midflap.png"),
                  pygame.image.load("flappy-bird-assets-master/sprites/yellowbird-upflap.png")]]

skyline_image = pygame.image.load("flappy-bird-assets-master/sprites/background-night.png")
daytime_image = pygame.image.load("flappy-bird-assets-master/sprites/background-day.png")
background_base = pygame.image.load("flappy-bird-assets-master/sprites/base.png")
up_wall = pygame.image.load("flappy-bird-assets-master/sprites/pipe-green.png")
down_wall = pygame.image.load("flappy-bird-assets-master/sprites/pipe-green.png")
loser_popup = pygame.image.load("flappy-bird-assets-master/sprites/gameover.png")
menu_page = pygame.image.load("flappy-bird-assets-master/sprites/message.png")
