import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('Pixeltype.ttf', 70)

sky_surface = pygame.image.load('sky.jpg').convert()
ground_surface = pygame.image.load('ground.jpg').convert()

score_surface = font.render('My game', False, (138, 54, 15))
score_rectangle = score_surface.get_rect(center=(600, 100))

hedgehog_surface = pygame.image.load('hedgehog_transparency.png').convert_alpha()
hedgehog_rectangle = hedgehog_surface.get_rect(bottomright=(1100, 600))

player_surface = pygame.image.load('player_transparency.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(200, 600))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom == 600:
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rectangle.bottom == 600:
                player_gravity = -20

        # if keys[pygame.K_RIGHT]:
        #     pass
        # if keys[pygame.K_LEFT]:
        #     pass

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 600))
    pygame.draw.rect(screen, (69, 139, 0), score_rectangle)
    pygame.draw.rect(screen, (69, 139, 0), score_rectangle, 20)

    screen.blit(score_surface, score_rectangle)

    hedgehog_rectangle.x -= 5
    if hedgehog_rectangle.right <= 0:
        hedgehog_rectangle.left = 1200
    screen.blit(hedgehog_surface, hedgehog_rectangle)
    # player_rectangle.left += 2

    # Player
    player_gravity += 1
    player_rectangle.y += player_gravity
    if player_rectangle.bottom >= 600:
        player_rectangle.bottom = 600
    screen.blit(player_surface, player_rectangle)

    mouse_position = pygame.mouse.get_pos()
    if player_rectangle.collidepoint(mouse_position):
        pygame.mouse.get_pressed()

    pygame.display.update()
    clock.tick(60)
