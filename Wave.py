import pygame
import random
pygame.init()

cd = 10
WH = WW = cd*50

cords = [[x,y] for y in range(0,WW,50) for x in range(0,WH,50)]

tiles = {
    'blank' : pygame.image.load('./Tiles/blank.png'),
    'up' : pygame.image.load('./Tiles/up.png'),
    'down' : pygame.image.load('./Tiles/down.png'),
    'left' : pygame.image.load('./Tiles/left.png'),
    'right' : pygame.image.load('./Tiles/right.png')
}

accupide = {str(cord) : 'None' for cord in cords}
print(accupide)

screen = pygame.display.set_mode((WH,WW))






running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    while x := True:
        screen.blit(tiles[insta_tile := random.choice(list(tiles))], insta_cord := random.choice(cords))
        accupide[str(insta_cord)] = insta_tile
        cords.remove(insta_cord)
        pygame.display.flip()
        pygame.time.wait(100)
        x = False
print(accupide)