def path_to_princess(grid):
	z = len(grid) - 1
	corners = [
		(0, 0), (0, z),
		(z, 0), (z, z)
	]

	p = next((r, c) for r, c in corners if grid[r][c] == 'p')
	m = (z // 2, z // 2)
	row_diff, col_diff = p[0] - m[0], p[1] - m[1]
	yield from (['UP'] * -row_diff if row_diff < 0 else ['DOWN'] * row_diff)
	yield from (['LEFT'] * -col_diff if col_diff < 0 else ['RIGHT'] * col_diff)

n = int(input())
grid = [input().strip() for _ in range(n)]
for move in path_to_princess(grid):
	print(move)