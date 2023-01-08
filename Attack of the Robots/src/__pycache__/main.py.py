import pygame
import random

# Start the game
pygame.init()
game_width = 1000
game_height = 600
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

background_image = pygame.image.load("../assets/BG_Sand.png")

# Make all the Sprites groups
playerGroup = pygame.sprite.Group()
projectilesGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()

# Put every Sprite class in a group
Player.containers = playerGroup
WaterBalloon.containers = projectilesGroup
Enemy.containers = enemiesGroup

enemy_spawn_timer_max = 80
enemy_spawn_timer = 0

mr_player = Player(screen, game_width/2, game_height/2)


# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Deal with player input (figure out what keys are playing pressed)        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        mr_player.move(1, 0)
    if keys[pygame.K_a]:
        mr_player.move(-1, 0)
    if keys[pygame.K_w]:
        mr_player.move(0, -1)
    if keys[pygame.K_s]:
        mr_player.move(0, 1)
    if pygame.mouse.get_pressed()[0]:
        mr_player.shoot()


    enemy_spawn_timer -= 1
    if enemy_spawn_timer <= 0:
        new_enemy = Enemy(screen, 0, 0, mr_player)
        side_to_spawn = random.randint(0,3)
        if side_to_spawn == 0:
            new_enemy.x = random.randint(0, game_width)
            new_enemy.y = -new_enemy.image.get_height()
        elif side_to_spawn == 1:
            new_enemy.x = random.randint(0, game_width)
            new_enemy.y = game_height + new_enemy.image.get_height()
        elif side_to_spawn == 2:
            new_enemy.x = -new_enemy.image.get_width()
            new_enemy.y = random.randint(0, game_height)
        elif side_to_spawn == 3:
            new_enemy.x = game_width + new_enemy.image.get_width()
            new_enemy.y = random.randint(0, game_height)
        enemy_spawn_timer = enemy_spawn_timer_max


        
    screen.blit(background_image, (0, 0))

    mr_player.update()

    for projectile in projectilesGroup:
        projectile.update()

    for enemy in enemiesGroup:
        enemy.update(projectilesGroup)



    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(40)
    pygame.display.set_caption("ATTACK OF THE ROBOTS fps: " + str(clock.get_fps()))
