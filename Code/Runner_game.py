import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'Score: {current_time}', False, 'Black')
    score_rectangle = score_surface.get_rect(center=(600, 100))
    screen.blit(score_surface, score_rectangle)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rectangle in obstacle_list:
            obstacle_rectangle.x -= randint(3, 8)

            if obstacle_rectangle.bottom == 600:
                screen.blit(hedgehog_surface, obstacle_rectangle)
            elif obstacle_rectangle.bottom == 599:
                screen.blit(snake_surface, obstacle_rectangle)
            elif obstacle_rectangle.bottom == 480:
                screen.blit(eagle_surface, obstacle_rectangle)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []


def collision(player, obstacles):
    if obstacles:
        for obstacles_rectangle in obstacles:
            if player.colliderect(obstacles_rectangle):
                return False
    return True


# def player_animation:
#     global player_walking_surface, player_index
#
#     if player_rectangle.bottom < 300:
#         player_walking_surface = player_jump
#         # jump animation if yoo want
#     else:
#         player_index += 0.1 # speed between every animation for the player
#         if player_index >= len(player_walk):
#             player_index = 0
#         player_walking_surface = player_walk[int(player_index)]
#         # walk animation if you want
#     # play animation from the player here

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('Pixeltype.ttf', 70)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('sky.jpg').convert()
ground_surface = pygame.image.load('ground.jpg').convert()

# score_surface = font.render('My game', False, (138, 54, 15))
# score_rectangle = score_surface.get_rect(center=(600, 100))

# Obstacles
hedgehog_surface = pygame.image.load('hedgehog_transparency.png').convert_alpha()
snake_surface = pygame.image.load('Snake_transparency.png').convert_alpha()
eagle_surface = pygame.image.load('Eagle_transparency.png').convert_alpha()

obstacles_rectangle_list = []

# Player
player_surface = pygame.image.load('player_transparency.png').convert_alpha()
# player_surface = pygame.image.load('# pictures what you want').convert_alpha() -
# player_jump = pygame.image.load('# pictures what you want').convert_alpha()
# if want to make animation uncomment line from above and put more pictures here
# can put as much as you want line here for a couple of animation
# put all variables in line from above in list
# player_index = 0 - uncomment this line too
# player_walking_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(midbottom=(200, 600))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('player_transparency.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rectangle = player_stand.get_rect(center=(600, 400))

# End screen
game_title = font.render('Minecraft Runner', False, (138, 54, 15))
game_title_rectangle = game_title.get_rect(center=(600, 150))
game_massage = font.render('Pres Enter to start a new run', False, (138, 54, 15))
game_massage_rectangle = game_massage.get_rect(center=(600, 600))
score_massage = font.render(f'Your score is: {score}', False, (138, 54, 15))
score_massage_rectangle = score_massage.get_rect(center=(600, 200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1600)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom == 600:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom == 600:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
            # if keys[pygame.K_RIGHT]:
            #     pass
            # if keys[pygame.K_LEFT]:
            #     pass

        # mouse_position = pygame.mouse.get_pos()
        # if player_rectangle.collidepoint(mouse_position):
        #     pygame.mouse.get_pressed()

        # if keys[pygame.K_RIGHT]:
        #     pass
        # if keys[pygame.K_LEFT]:
        #     pass
        if event.type == obstacle_timer:
            if game_active:
                if randint(0, 2):
                    obstacles_rectangle_list.append(hedgehog_surface.get_rect(bottomright=((randint(1300, 1800)), 600)))
                elif randint(0, 2):
                    obstacles_rectangle_list.append(snake_surface.get_rect(bottomright=((randint(1300, 1800)), 599)))
                elif randint(0, 2):
                    obstacles_rectangle_list.append(eagle_surface.get_rect(bottomright=(randint(1300, 1800), 480)))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 600))
        score = display_score()

        # hedgehog_rectangle.x -= 5
        # if hedgehog_rectangle.right <= 0:
        #     hedgehog_rectangle.left = 1200
        # screen.blit(hedgehog_surface, hedgehog_rectangle)
        # player_rectangle.left += 2

        # Player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 600:
            player_rectangle.bottom = 600
        # player_animation()
        screen.blit(player_surface, player_rectangle)

        # Obstacle movement
        obstacles_rectangle_list = obstacle_movement(obstacles_rectangle_list)

        # Collision
        game_active = collision(player_rectangle, obstacles_rectangle_list)
    else:
        screen.fill((93, 129, 162))
        screen.blit(player_stand, player_stand_rectangle)
        screen.blit(game_title, game_title_rectangle)
        screen.blit(game_massage, game_massage_rectangle)
        obstacles_rectangle_list.clear()
        player_rectangle.midbottom = (200, 600)
        player_gravity = 0

        score_massage = font.render(f'Your score is: {score}', False, (138, 54, 15))
        score_massage_rectangle = score_massage.get_rect(center=(600, 200))
        screen.blit(score_massage, score_massage_rectangle)

    pygame.display.update()
    clock.tick(60)
