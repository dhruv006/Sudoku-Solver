import numpy as np

puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def rules(x,y,n):
	global puzzle
	for i in range(0,9):
		if puzzle[y][i] == n:
			return False
	for i in range(0,9):
		if puzzle[i][x] == n:
			return False
	y0 = (y//3)*3
	x0 = (x//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if puzzle[y0+i][x0+j] == n:
				return False
	return True

def solvePuzzle():
	global puzzle
	for y in range(0,9):
		for x in range(0,9):
			if puzzle[y][x] == 0:
				for n in range(1,10):
					if rules(x,y,n):
						puzzle[y][x] = n
						solvePuzzle()
						puzzle[y][x] = 0
				return
	print(np.matrix(puzzle))

solvePuzzle()