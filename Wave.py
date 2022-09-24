import pygame
pygame.init()

WH = WW = 400
screen = pygame.display.set_mode((WH,WW))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False