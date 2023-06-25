import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("PingPong")

game_is_active = True

clock = pygame.time.Clock()

while game_is_active:
    # Check if user did an action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_active = False

    pygame.display.flip()

    # Make refresh times
    clock.tick(60)

pygame.quit()
