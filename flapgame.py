import pygame, sys
import random
import assets as ast
import settings as set
from birdiemurdie import Bird
from back_movable import Ground
from walls import Pipe
from os import path

global highscore, backchoice

pygame.init()
clock = pygame.time.Clock()
display_surf = pygame.display.set_mode((set.win_width, set.win_height))
game_stopped = True

dir = path.dirname(__file__)
with open("HS_FILE.txt", 'r') as f:
    try:
        set.highscore = int(f.read())
    except:

        set.highscore = 0

font = pygame.font.Font("flappy-bird-assets-master/flappy-font.ttf", 40)
font2 = pygame.font.Font("flappy-bird-assets-master/flappy-font.ttf", 20)
backchoice = 0

def quit_game():
    # Exit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


# Game Main Method
def main():
    first = False
    # Instantiate Bird
    bird = pygame.sprite.GroupSingle()
    bird.add(Bird(random.randint(0, 2)))

    # Setup Pipes
    pipe_timer = 0
    pipes = pygame.sprite.Group()

    # Instantiate Initial Ground
    x_pos_ground, y_pos_ground = 0, 400
    ground = pygame.sprite.Group()
    ground.add(Ground(x_pos_ground, y_pos_ground))
    backchoice = random.choice([0,1])

    run = True
    while run:
        # Quit
        quit_game()

        # Reset Frame
        display_surf.fill((0, 0, 0))

        # User Input
        presser = pygame.key.get_pressed()

        # Draw Background
        if backchoice == 1:
            display_surf.blit(ast.skyline_image, (0, 0))
        else:
            display_surf.blit(ast.daytime_image, (0, 0))

        # Spawn Ground
        if len(ground) <= 2:
            ground.add(Ground(set.win_width, y_pos_ground))

        # Draw - Pipes, Ground and Bird
        pipes.draw(display_surf)
        ground.draw(display_surf)
        bird.draw(display_surf)

        # Show Score
        score_text = font.render(str(set.score), True, pygame.Color(255, 255, 255))
        display_surf.blit(score_text, (set.win_width / 2 - 10, set.win_height / 50 + 20))
        # It is getting harder! At every 5 pipes!
        if set.score > set.level + 5:
            set.level += 1
            set.scroll_speed += 1

        # Update - Pipes, Ground and Bird
        if bird.sprite.alive:
            pipes.update()
            ground.update()
        bird.update(presser)

        # Collision Detection
        collision_pipes = pygame.sprite.spritecollide(bird.sprites()[0], pipes, False)
        collision_ground = pygame.sprite.spritecollide(bird.sprites()[0], ground, False)
        if collision_pipes or collision_ground:
            if not first:
                music = pygame.mixer.Sound("flappy-bird-assets-master/audio/hit.wav")
                music.play(loops = 0)
                music = pygame.mixer.Sound("flappy-bird-assets-master/audio/die.wav")
                music.play(loops = 0)
                first = True
            bird.sprite.alive = False

            display_surf.blit(ast.loser_popup, (set.win_width // 2 - ast.loser_popup.get_width() // 2,
                                                set.win_height // 2 - ast.loser_popup.get_height() // 2 - 50))
            if set.score > set.highscore:
                set.highscore = set.score
                with open("HS_FILE.txt", 'w') as f:
                    f.write(str(set.highscore))
            highscore_text = font2.render("BEST: " + str(set.highscore), True, pygame.Color(255, 255, 255))
            display_surf.blit(highscore_text, (set.win_width / 2 - 40, set.win_height / 2))
            highscore_text = font2.render(str("PRESS ENTER"), True, pygame.Color(255, 255, 255))
            display_surf.blit(highscore_text, (set.win_width / 2 - 65, set.win_height / 2 + 25))

            if presser[pygame.K_RETURN]:
                set.score = 0
                break

        # Spawn Pipes
        if pipe_timer <= 0 and bird.sprite.alive:
            x_top, x_bottom = 288, 288
            y_top = random.randint(-250, -150)
            y_bottom = y_top + random.randint(90, 130) + ast.down_wall.get_height()
            pipes.add(Pipe(x_top, y_top, ast.up_wall, 'top'))
            pipes.add(Pipe(x_bottom, y_bottom, ast.down_wall, 'bottom'))
            pipe_timer = random.randint(180, 250)
        pipe_timer -= 1*set.scroll_speed

        clock.tick(60)
        pygame.display.update()


# Menu
def menu():
    global game_stopped
    bird = pygame.sprite.GroupSingle()
    rand = random.randint(0, 2)
    bird.add(Bird(rand))


    while game_stopped:
        quit_game()

        # Draw Menu
        display_surf.fill((0, 0, 0))
        if backchoice == 1:
            display_surf.blit(ast.skyline_image, (0, 0))
        else:
            display_surf.blit(ast.daytime_image, (0, 0))
        display_surf.blit(ast.background_base, Ground(0, 480))
        display_surf.blit(ast.birdie_skins[rand][0], (100, 250))
        display_surf.blit(ast.menu_page, (set.win_width // 2 - ast.menu_page.get_width() // 2,
                                          set.win_height // 2 - ast.menu_page.get_height() // 2))
        highscore_text = font2.render("BEST: " + str(set.highscore), True, pygame.Color(255, 255, 255))
        display_surf.blit(highscore_text, (set.win_width / 2 - 40, set.win_height / 2 - 200))

        # User Input
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            main()

        pygame.display.update()


if __name__ == '__main__':
    menu()