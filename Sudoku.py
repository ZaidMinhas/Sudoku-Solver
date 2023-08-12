
class Sudoku:
	def __init__(self, board):
		self.board = [[Cell(small) for small in big] for big in board]
		
		
	def print(self, symbol = "#"):
		print()
		for i in range(0,9,3):
			for j in range(0,9,3):
				print(f"{symbol} " +  f" {symbol} ".join([" ".join(map( str, self.board[i+k][j:j+3])) for k in range(3)]) + f" {symbol}")
			print(f"{symbol} "*13)
		print()

	def printPos(self):
		for i in range(9):
			for j in range(9):
				if (self.board[i][j].value == 0):
					print(self.board[i][j].pos)
			print()

	def solve(self):
		while True:
			if (not self.sieve()):
				break

	def shave(self):
		
		changes = False
		for big in range(9):
			for small in range(9):
				cell = self.board[big][small]
				if (cell.value == 0):
					self.checkBig(cell, big, small)
					self.checkRow(cell, big, small)
					self.checkCol(cell, big, small)

					if len(cell.pos) == 1:
						cell.value = cell.pos[0]
						cell.pos = None
						
						changes = True
		return changes

	def checkBig(self,cell, big, small):
		check = [i for i in range(9)]
		check.remove(small)
		for i in check:
			check_cell = self.board[big][i]
			if (check_cell.value != 0 and check_cell.value in cell.pos):
				cell.pos.remove(check_cell.value)

	def checkRow(self, cell, big, small):
		check_big = [3*(big//3) + i for i in range(3)]
		check_big.remove(big)

		check_small = [3*(small//3) + i for i in range(3)]

		for big in check_big:
			for small in check_small:
				check_cell = self.board[big][small]
				if (check_cell.value != 0 and check_cell.value in cell.pos):
					cell.pos.remove(check_cell.value)

	def checkCol(self, cell, big, small):
			check_big = [(big%3) + i*3 for i in range(3)]
			check_big.remove(big)

			check_small = [(small%3) + i*3 for i in range(3)]
			for big in check_big:
				for small in check_small:
					check_cell = self.board[big][small]
					if (check_cell.value != 0 and check_cell.value in cell.pos):
						cell.pos.remove(check_cell.value)


	def sieve(self):
		changes = False

		while (True):	
			check = self.shave()
			changes |= check
			if (not check):
				break


		for big in range(9):
			changes |= self.sieveBox(big)
		
		while (True):	
			check = self.shave()
			changes |= check
			if (not check):
				break


		for big in range(0,9,3):
			for small in range(0,9,3):
				changes |= self.sieveRow(big, small)
		
		while (True):	
			check = self.shave()
			changes |= check
			if (not check):
				break


		for big in range(3):
			for small in range(3):
				changes |= self.sieveCol(big, small)

		return changes

		

	def sieveBox(self, big):
		changes = False
		totalPos = []
		for small in range(9):
			cell = self.board[big][small]
			if (cell.pos != None):
				totalPos += cell.pos

		if len(totalPos) == 0:
			return False

		counter = {}
		for i in set(totalPos):
			counter.update({i : totalPos.count(i)})

		sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1]))


		if (list(sorted_counter.values())[0] == 1):
			value = list(sorted_counter.keys())[0]
			for small in range(9):
				cell = self.board[big][small]
				if (cell.pos != None and value in cell.pos):
					cell.value = value
					cell.pos = None
					
					changes = True
					break
		return changes

	def sieveRow(self, big, small):
		changes = False
		totalPos = []
		check_big = [3*(big//3) + i for i in range(3)]
		check_small = [3*(small//3) + i for i in range(3)]
		for big in check_big:
			for small in check_small:
				cell = self.board[big][small]
				if (cell.pos != None):
					totalPos += cell.pos

		if len(totalPos) == 0:
			return False
			
		counter = {}
		for i in set(totalPos):
			counter.update({i : totalPos.count(i)})

		sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1]))

		if (list(sorted_counter.values())[0] == 1):
			value = list(sorted_counter.keys())[0]
			for big in check_big:
				for small in check_small:
					cell = self.board[big][small]	
					if (cell.pos != None and value in cell.pos):
						cell.value = value
						cell.pos = None
						
						changes= True
						break
		return changes

	def sieveCol(self, big, small):
			changes = False
			totalPos = []
			check_big = [(big%3) + i*3 for i in range(3)]
			check_small = [(small%3) + i*3 for i in range(3)]

			for big in check_big:
				for small in check_small:
					cell = self.board[big][small]
					if (cell.pos != None):
						totalPos += cell.pos

			if len(totalPos) == 0:
				return False
			
			counter = {}
			for i in set(totalPos):
				counter.update({i : totalPos.count(i)})

			sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1]))

			if (list(sorted_counter.values())[0] == 1):
				value = list(sorted_counter.keys())[0]
				for big in check_big:
					for small in check_small:
						cell = self.board[big][small]	
						if (cell.pos != None and value in cell.pos):
							cell.value = value
							cell.pos = None
							
							changes = True
							break
			return changes
						
					
class Cell:
	def __init__(self, value):
		self.value = value
		self.pos = None
		if (value == 0):
			self.pos = [1,2,3,4,5,6,7,8,9]

	def __repr__(self):
		return str(self.value)


#enter data grid by grid
board = [
	[0,5,0,7,0,2,0,0,9],
	[0,0,8,0,4,3,0,0,0],
	[2,6,9,0,0,0,0,0,0],
	[0,0,7,0,0,0,5,0,3],
	[0,0,0,0,9,0,0,0,0],
	[0,0,0,0,4,0,0,9,0],
	[0,0,0,6,0,0,0,4,0],
	[0,2,4,0,0,0,0,8,0],
	[6,0,5,0,0,3,0,0,0]
	]
game = Sudoku(board)
game.print(" ")
game.solve()
print("#"*50)
game.print(" ")