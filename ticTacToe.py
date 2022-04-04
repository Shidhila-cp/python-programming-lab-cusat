import pygame,sys
import numpy as np

pygame.init()

width = 600
height = 600
black = (0, 0, 0)
bg_color = (76, 5, 141)
line_width = 10
board_rows = 3
board_coloumns = 3

board = np.zeros((board_rows,board_coloumns))
print(board)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(bg_color)
#pygame.draw.line(screen,black,(10,10),(300,300),10)

def draw_lines():
  pygame.draw.line(screen,black,(0,200),(600,200),line_width)
  pygame.draw.line(screen,black,(0,400),(600,400),line_width)
  pygame.draw.line(screen,black,(200,0),(200,600),line_width)
  pygame.draw.line(screen,black,(400,0),(400,600),line_width)

def mark_square(rows,cols,player):
  board[rows][cols] = player

def available_square(rows,cols):
  return board[rows][cols] == 0

mark_square(0,0,1)
print(available_square(0,0))
draw_lines()

while True:
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       sys.exit()

   pygame.display.update()