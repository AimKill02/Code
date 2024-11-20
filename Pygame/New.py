import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_radius = 40

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LSHIFT]:
        move_speed = 200
    else:
        move_speed = 600

    if keys[pygame.K_w]:
        player_pos.y -= move_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += move_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= move_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += move_speed * dt

    player_pos.x = max(player_radius, min(screen.get_width() - player_radius, player_pos.x))
    player_pos.y = max(player_radius, min(screen.get_height() - player_radius, player_pos.y))

    pygame.draw.circle(screen, 'red', player_pos, player_radius)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()