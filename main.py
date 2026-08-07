import warnings
warnings.filterwarnings('ignore',category=RuntimeWarning)

import pygame
import random
from assets import *

pygame.init()

positions=[(row,col) for row in range(ROWS) for col in range(COLS)]
bombPos=random.sample(positions,bombCount)

for row,col in bombPos:
	bombs[row][col]=1
	board[row][col]='b'

pygame.display.set_caption('Minesweeper')

WIN.fill((0,0,0))

bomb_count()

for row in range(ROWS):
	for col in range(COLS):
		'''if bombs[row][col]==1:
			WIN.blit(BOMB,(row*32,col*32))'''
		WIN.blit(CLOSE,(row*32,col*32))


pygame.display.update()
print(board)

run=True
while run:
	
	x=pygame.mouse.get_pos()[0]//32;y=pygame.mouse.get_pos()[1]//32

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
			break
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.button==3:
				if flags[x][y]==1:
					WIN.blit(CLOSE,(x*32,y*32))
					flagCount+=1
					flags[x][y]=0
				elif flagCount>0:
					WIN.blit(FLAG,(x*32,y*32))
					flagCount-=1
					flags[x][y]=1
					
			if event.button==1:
				if board[x][y]!='b':
					openEmpty(x,y)
				elif board[x][y]=='b':
					for i in range(ROWS):
						for j in range(COLS):
							if board[i][j]=='b':
								WIN.blit(BOMB,(i*32,j*32))
					run=False
					break
	if check_finished():
		print("You Win!")
		run=False

	keys=pygame.key.get_pressed()
	if keys[pygame.K_q]:
		run=False
		break

	pygame.display.update()

pygame.quit()
