import pygame
import random
pygame.init()

DIM = 500
WH = WW = DIM/4

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

tiles = {
    'blank' : pygame.transform.scale(pygame.image.load('./Tiles/blank.png'), (WH, WW)),
    'up' : pygame.transform.scale(pygame.image.load('./Tiles/up.png'), (WH, WW)),
    'down' : pygame.transform.scale(pygame.image.load('./Tiles/down.png'), (WH, WW)),
    'left' : pygame.transform.scale(pygame.image.load('./Tiles/left.png'), (WH, WW)),
    'right' : pygame.transform.scale(pygame.image.load('./Tiles/right.png'), (WH, WW))
}

rules = {
    'blank' : [['blank', 'up'], ['blank', 'down'], ['blank', 'left'], ['blank', 'right']],
    'up' : [['down', 'left', 'right'], ['blank', 'down'], ['up', 'down', 'right'], ['up', 'down', 'left']],
    'down' : [['blank', 'up'], ['up', 'left', 'right'], ['up', 'down', 'right'], ['up', 'down', 'left']],
    'left' : [['down', 'left', 'right'], ['up', 'left', 'right'], ['up', 'down', 'right'], ['blank', 'right']],
    'right' : [['down', 'left', 'right'], ['up', 'left', 'right'], ['blank', 'left'], ['up', 'down', 'left']]
}

screen = pygame.display.set_mode((DIM,DIM))




screen.blit(tiles[random.choice(list(tiles.keys()))], (random.randrange(0, DIM, WW), random.randrange(0, DIM, WH)))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    


    pygame.display.flip()
    
    