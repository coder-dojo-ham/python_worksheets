import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
is_blue = True
x = 30
y = 30
x2 = 100
y2 = 100

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3

    if pressed[pygame.K_w]:
        y2 -= 3
    if pressed[pygame.K_s]:
        y2 += 3
    if pressed[pygame.K_a]:
        x2 -= 3
    if pressed[pygame.K_d]:
        x2 += 3

    screen.fill((0, 0, 0))

    if is_blue:
        color1 = (0, 128, 255)
        color2 = (255, 100, 0)
    else:
        color1 = (255, 100, 0)
        color2 = (0, 128, 255)

    rect1 = pygame.Rect(x, y, 60, 60)
    rect2 = pygame.Rect(x2, y2, 60, 60)

    if rect1.colliderect(rect2):
        break

    pygame.draw.rect(screen, color1, rect1)
    pygame.draw.rect(screen, color2, rect2)

    pygame.display.flip()
    clock.tick(60)
