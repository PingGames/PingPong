import pygame
import os

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("PingPong")

image_folder = "extra/images"
image_path = os.path.join(image_folder, "ball.png")
ball_image = pygame.image.load(image_path).convert_alpha()


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = ball_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass


all_sprites = pygame.sprite.Group()

ball = Ball(295, 215)
all_sprites.add(ball)


game_is_active = True

clock = pygame.time.Clock()

while game_is_active:
    # Check if user did an action
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_active = False

    screen.fill((255, 255, 255))

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()

    # Make refresh times
    clock.tick(60)

pygame.quit()
