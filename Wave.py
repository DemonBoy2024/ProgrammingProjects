import pygame
import random
import sys
pygame.init()


#Checks for any cells with 0 possible tiles
def no_empty_tile(board):
  for i in board:
    if len(board) == 0:
      return False
  return True


#Takes in the index of the cell in the list board and outputs the coordinate it holds on the canvas
def coord_index(row, col):
  return [row*tile_height, col*tile_width]

def possibility_collapse(current_cell_index):
  return 0
  
  



window_width = window_height = 400
tile_width = tile_height = window_width/4
cells_in_row = int(window_width/tile_width)
number_of_rows = int(window_height/tile_height)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


#Stores tile images
tiles = {
  'blank' : pygame.transform.scale(pygame.image.load('./Tiles/blank.png'), (tile_width, tile_height)),
  'up' : pygame.transform.scale(pygame.image.load('./Tiles/up.png'), (tile_width, tile_height)),
  'down' : pygame.transform.scale(pygame.image.load('./Tiles/down.png'), (tile_width, tile_height)),
  'left' : pygame.transform.scale(pygame.image.load('./Tiles/left.png'), (tile_width, tile_height)),
  'right' : pygame.transform.scale(pygame.image.load('./Tiles/right.png'), (tile_width, tile_height))
}

#Sets rules for each tile
rules = {
    'blank' : [['blank', 'up'], ['blank', 'down'], ['blank', 'left'], ['blank', 'right']],
    'up' : [['down', 'left', 'right'], ['blank', 'down'], ['up', 'down', 'right'], ['up', 'down', 'left']],
    'down' : [['blank', 'up'], ['up', 'left', 'right'], ['up', 'down', 'right'], ['up', 'down', 'left']],
    'left' : [['down', 'left', 'right'], ['up', 'left', 'right'], ['up', 'down', 'right'], ['blank', 'right']],
    'right' : [['down', 'left', 'right'], ['up', 'left', 'right'], ['blank', 'left'], ['up', 'down', 'left']]
}

#Creates board with superposition of all possible cells
board = [[['blank', 'up', 'down', 'left', 'right'] for x in range(0, cells_in_row)] for i in range(0, number_of_rows)]
collapsed_cell = [[False for x in range(0, cells_in_row)] for i in range(0, number_of_rows)]


#Draws screen with black background
screen = pygame.display.set_mode((window_height, window_width))
screen.fill((255,255,255))


#Places random tile at random cell and collapses that cell to that tile in the board list
rand_tile = random.choice(list(tiles.keys()))
col, row = random.randint(0, cells_in_row - 1), random.randint(0, number_of_rows - 1)
screen.blit(tiles[rand_tile], coord_index(col, row))
board[row][col] = [rand_tile]
collapsed_cell[row][col]


while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             sys.exit()
    pygame.display.flip()