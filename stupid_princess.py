def nextmove(n, r, c, grid):
	# Find the Princess
	for i in range(n):
		for j in range(n):
			if grid[i][j] == "p":
				princess_row = i
				princess_col = j
				break
	# Calculate the difference from the provided
	# Row, column and princess
	row_diff = princess_row - r
	col_diff = princess_col - c

	if row_diff > 0:
		return("DOWN")
	elif row_diff < 0:
		return("UP")
	elif col_diff > 0:
		return("RIGHT")
	elif col_diff < 0:
		return("LEFT")
	else:
		return("I'm there!")

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
	grid.append(input())

print(nextmove(n,r,c,grid))
