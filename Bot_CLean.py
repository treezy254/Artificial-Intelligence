def next_move(posr, posc, board):
	i, j = min(((i, j) for i, row in enumerate(board) if 'd' in row for j, c in enumerate(row) if c == 'd'),
			key = lambda x: abs(posr - x[0] + abs(posc - x[1]))

	if j < posc:
		print("LEFT")
	elif j > posc:
		print("RIGHT")
	elif i < posr:
		print("UP")
	elif i > posr:
		print("DOWN")

	else:
		print("CLEAN")