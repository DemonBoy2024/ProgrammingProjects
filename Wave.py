import pygame
import random
import sys
pygame.init()

window_width = window_height = 400
tile_width = tile_height = window_width/8
cells_in_row = int(window_width/tile_width)
number_of_rows = int(window_height/tile_height)

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
  

#Checks for any cells with 0 possible tiles
def no_empty_tile(board):
  for i in board:
    if len(board) == 0:
      return False
  return True


#Takes in the index of the cell in the list board and outputs the coordinate it holds on the canvas
def coord_index(row, col):
  return [row*tile_height, col*tile_width]

def possibility_collapse(cellY, cellX, state):
  

  if collapsed_cell[cellY][cellX] is False:
    board[cellY][cellX] = random.choice(board[cellY][cellX])
    collapsed_cell[cellY][cellX] = True

  
    
  #Cell above
  correct_opts = []
  if cellY != 0 and collapsed_cell[cellY-1][cellX] != True:  
    if collapsed_cell[cellY-1][cellX] is False:
      for opt in board[cellY-1][cellX]:
        if opt in rules[state[0]][UP]:
          #board[cellY-1][cellX].remove(opt)
          correct_opts.append(opt)
    board[cellY-1][cellX] = correct_opts
    
  

  #Cell below
  correct_opts = []
  if cellY != number_of_rows-1 and collapsed_cell[cellY+1][cellX] != True:
    if collapsed_cell[cellY+1][cellX] is False:
      for opt in board[cellY+1][cellX]:
        if opt in rules[state[0]][DOWN]:
          #board[cellY-1][cellX].remove(opt)
          correct_opts.append(opt)
    board[cellY+1][cellX] = correct_opts
        
  #Cell to the left
  correct_opts = []
  if cellX != 0 and collapsed_cell[cellY][cellX-1] != True:
    if collapsed_cell[cellY][cellX-1] is False:
      for opt in board[cellY][cellX-1]:
        if opt in rules[state[0]][LEFT]:
          #board[cellY-1][cellX].remove(opt)
          correct_opts.append(opt)
    board[cellY][cellX-1] = correct_opts
  
  #Cell to the right
  correct_opts = []
  if cellX != cells_in_row-1 and collapsed_cell[cellY][cellX+1] != True:
    if collapsed_cell[cellY][cellX+1] is False:
      for opt in board[cellY][cellX+1]:
        if opt in rules[state[0]][RIGHT]:
          #board[cellY-1][cellX].remove(opt)
          correct_opts.append(opt)  
    board[cellY][cellX+1] = correct_opts

# Returns list of ajcent cell cords that arent collapsed
def possible_adj_cord(cellY, cellX) -> list(tuple()):
  adj_cells = []
  if cellY != 0:
    if not collapsed_cell[cellY-1][cellX]:
      adj_cells.append((cellY-1, cellX))
  if cellY != number_of_rows-1:
    if not collapsed_cell[cellY+1][cellX]:
      adj_cells.append((cellY+1, cellX))

  if cellX != 0:
    if not collapsed_cell[cellY][cellX-1]:
      adj_cells.append((cellY, cellX-1))
  if cellX != cells_in_row-1:
    if not collapsed_cell[cellY][cellX+1]:
      adj_cells.append((cellY, cellX+1))
  
  return adj_cells

# Returns cords of adjacent cell with the least possibilities
def lowest_opt_adj_cell(cellY, cellX):

  positions = possible_adj_cord(cellY, cellX)
  if len(positions) != 0:
    lowest_opt = (positions[0])
  
    num = len(board[positions[0][0]][positions[0][1]])
    for i in positions:
      len_of_neighbor = len(board[i[0]][i[1]])
      if len_of_neighbor < num and len_of_neighbor > 0:
        lowest_opt = i
        num = len(board[i[0]][i[1]])
    return lowest_opt
  return None






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
rand_tile = random.choice(list(tiles.keys())[1:])
col, row = random.randint(0, cells_in_row - 1), random.randint(0, number_of_rows - 1)
screen.blit(tiles[rand_tile], coord_index(col, row))
board[row][col] = [rand_tile]
current_cellY = row
current_cellX = col
collapsed_cell[row][col]

'''for x in board:
  print(x)
print()'''
possibility_collapse(row, col, board[row][col])
'''for x in board:
  print(x)


for x in board:
  print(x)
'''
new_cell_cord = lowest_opt_adj_cell(row, col)
#print(new_cell_cord)







while any(False in i for i in collapsed_cell):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             sys.exit()
    if new_cell_cord != None: 
      new_row = new_cell_cord[0]
      new_col = new_cell_cord[1]
      if collapsed_cell[new_cell_cord[0]][new_cell_cord[1]] == False:
        new_row = new_cell_cord[0]
        new_col = new_cell_cord[1]
        board[new_row][new_col] = list(filter(None, board[new_row][new_col]))
        #print(board[new_row][new_col])
        collapsed_cell[new_row][new_col] = True
        board[new_row][new_col] = [random.choice(board[new_row][new_col])] if len(board[new_row][new_col]) > 1 else board[new_row][new_col]
        print(new_cell_cord)
        print(board[2][0])
        print(board[new_row][new_col])
        
        screen.blit(tiles[board[new_row][new_col][0]], coord_index(new_col, new_row))
        
        possibility_collapse(new_row, new_col, board[new_row][new_col])
        new_cell_cord = lowest_opt_adj_cell(new_row, new_col)
      
    else:
      for i in range(len(board)):
        for x in range(len(board)):
          if collapsed_cell[i][x] != True:
            board[i][x] = [random.choice(board[i][x])]
            break
      '''print(i, x)'''
      #print(board[i][x])
      possibility_collapse(i, x, board[i][x])
      screen.blit(tiles[board[i][x]], coord_index(x, i))
      collapsed_cell[new_row][new_col] = True
      new_cell_cord = lowest_opt_adj_cell(i, x)
      print('\t', new_cell_cord)
      print('\t', board[new_cell_cord[0]][new_cell_cord[1]])
      #print(new_cell_cord)
    pygame.time.wait(250)
  
    pygame.display.flip()