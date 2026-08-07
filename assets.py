import pygame

ROWS=9
COLS=9

WIDTH,HEIGHT=ROWS*32,COLS*32
WIN=pygame.display.set_mode((WIDTH,HEIGHT))

BOMB=pygame.image.load('Assets/bomb.png')
CLOSE=pygame.image.load('Assets/close.png')
OPEN=pygame.image.load('Assets/open.png')
FLAG=pygame.image.load('Assets/flag.png')
EIGHT=pygame.image.load('Assets/eight.png')
SEVEN=pygame.image.load('Assets/seven.png')
SIX=pygame.image.load('Assets/six.png')
FIVE=pygame.image.load('Assets/five.png')
FOUR=pygame.image.load('Assets/four.png')
THREE=pygame.image.load('Assets/three.png')
TWO=pygame.image.load('Assets/two.png')
ONE=pygame.image.load('Assets/one.png')

numMap={
	0: OPEN,
	1: ONE,
	2: TWO,
	3: THREE,
	4: FOUR,
	5: FIVE,
	6: SIX,
	7: SEVEN,
	8: EIGHT,
}

bombs=[[0]*ROWS for i in range(COLS)]
board=[[0]*ROWS for i in range(COLS)]
flags=[[0]*ROWS for i in range(COLS)]
opened=[[0]*ROWS for i in range(COLS)]

flagCount=10
bombCount=10

def bomb_count():
	for x in range(ROWS):
		for y in range(COLS):
			if bombs[x][y]==0:
				count=0
				for dx in [-1,0,1]:
					for dy in [-1,0,1]:
						if dx==0 and dy==0:
							continue
						nx,ny=x+dx,y+dy
						if 0<=nx<ROWS and 0<=ny<COLS:
							if bombs[nx][ny]==1:
								count+=1
				board[x][y]=count

def openEmpty(x,y):
	if not (0<=x<ROWS and 0<=y<COLS):
		return
	if board[x][y]=='b':
		return
	
	WIN.blit(numMap[board[x][y]],(x*32,y*32))
	opened[x][y]=1

	if board[x][y]==0:
		for dx in [-1,0,1]:
			for dy in [-1,0,1]:
				if dx==0 and dy==0:
					continue
				nx,ny=dx+x,dy+y
				if 0<=nx<ROWS and 0<=ny<COLS:
					if opened[nx][ny]==0:
						openEmpty(nx,ny)

def check_finished():
	for x in range(ROWS):
		for y in range(COLS):
			if bombs[x][y]!=flags[x][y]:
				return False
	return True
