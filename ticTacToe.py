import pygame,sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
BLACK = (0, 0, 0)
RED = (255,0,0)
BG_COLOR = (76, 5, 141)
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLUMNS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 10
SPACE = 45

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

#board
board = np.zeros((BOARD_ROWS,BOARD_COLUMNS))
print(board)


#pygame.draw.line(screen,black,(20,20),(580,580),15)
def draw_lines():
  #horizontal - lines
  pygame.draw.line(screen,BLACK,(0,200),(600,200),LINE_WIDTH)
  pygame.draw.line(screen,BLACK,(0,400),(600,400),LINE_WIDTH)
  #vertical - lines
  pygame.draw.line(screen,BLACK,(200,0),(200,600),LINE_WIDTH)
  pygame.draw.line(screen,BLACK,(400,0),(400,600),LINE_WIDTH)

def draw_figures():
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLUMNS):
      if board[row][col]==1:
        pygame.draw.circle(screen,BLACK, (int ((col*200)+100),int((row*200)+100)),CIRCLE_RADIUS,CIRCLE_WIDTH)
      elif board[row][col]==2:
        pygame.draw.line(screen,BLACK,(col*200+SPACE,(row*200+200)-SPACE),((col*200+200)-SPACE,(row*200)+SPACE),15)
        pygame.draw.line(screen,BLACK,(col*200+SPACE,(row*200)+SPACE),((col*200+200)-SPACE,(row*200+200)-SPACE),15)

def mark_square(rows,cols,player):
  board[rows][cols] = player

def available_square(rows,cols):
  return board[rows][cols] == 0

def is_board_full():
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLUMNS):
      if(board[row][col]==0):
        return False
      else:
        return True

def check_win(player):
  #vertical-win-check
  for col in range(BOARD_COLUMNS):
    if board[0][col] ==player and board[1][col] ==player and board[2][col] ==player:
      draw_vertical_winning_line(col,player)
      return True
  #horizontal-win-check
  for row in range(BOARD_ROWS):
    if board[row][0] ==player and board[row][1] ==player and board[row][2] ==player:
      draw_horizontal_winning_line(row,player)
      return True
  #ascending-diagonal-win-check
  if board[2][0]==player and board[1][1]==player and board[0][2]==player:
    draw_ascending_diagonal_winning_line(player)
    return True
  #descending-diagonal-win-check
  if board[0][0]==player and board[1][1]==player and board[2][2]==player:
    draw_descending_diagonal_winning_line(player)
    return True
  return False

def draw_vertical_winning_line(col,player):
  pygame.draw.line(screen,RED,(col*200+100,0),(col*200+100,600),15)

def draw_horizontal_winning_line(row,player):
  pygame.draw.line(screen,RED,(0,row*200+100),(600,row*200+100),15)

def draw_ascending_diagonal_winning_line(player):
  pygame.draw.line(screen,RED,(15,HEIGHT-15),(WIDTH-15,15),15)

def draw_descending_diagonal_winning_line(player):
  pygame.draw.line(screen,RED,(15,15),(WIDTH-15,HEIGHT-15),15)

def restart():
  screen.fill(BG_COLOR)
  draw_lines()
  game_over = False
  player = 1
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLUMNS):
      board[row][col]=0

# mark_square(0,0,1)
# print(board)
# mark_square(1,1,2)
# print(board)
# print(available_square(0,0))
# print(available_square(1,1))

draw_lines()

game_over = False
player = 1

#main loop
while True:
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       sys.exit()
     if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
       mouseX  = event.pos[0] #x
       mouseY = event.pos[1] #y
       clicked_row = int(mouseY//200)
       clicked_col = int(mouseX//200)
       if available_square(clicked_row,clicked_col):
         if player==1:
           mark_square(clicked_row,clicked_col,1)
           if check_win(player):
             game_over = True
           player = 2
         elif player == 2:
           mark_square(clicked_row,clicked_col,2)
           if check_win(player):
             game_over = True
           player = 1
         draw_figures()
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          print("R is Pressed")
          restart()
          player = 1
          game_over = False
   pygame.display.update()
