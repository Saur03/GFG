'''
Find shortest safe route in a path with landmines.
Given a path in the form of a rectangular matrix having few landmines arbitrarily placed (marked as 0), 
calculate length of the shortest safe route possible from any cell in the first column 
to any cell in the last column of the matrix. 

We have to avoid landmines and their four adjacent cells (left, right, above and below) as they are also unsafe. 
We are allowed to move to only adjacent cells which are not landmines. i.e. the route cannot contains any diagonal moves.

Examples:  

Input: 
A 12 x 10 matrix with landmines marked as 0

[ 1  1  1  1  1  1  1  1  1  1 ]
[ 1  0  1  1  1  1  1  1  1  1 ]
[ 1  1  1  0  1  1  1  1  1  1 ]
[ 1  1  1  1  0  1  1  1  1  1 ]
[ 1  1  1  1  1  1  1  1  1  1 ]
[ 1  1  1  1  1  0  1  1  1  1 ]
[ 1  0  1  1  1  1  1  1  0  1 ]
[ 1  1  1  1  1  1  1  1  1  1 ]
[ 1  1  1  1  1  1  1  1  1  1 ]
[ 0  1  1  1  1  0  1  1  1  1 ]
[ 1  1  1  1  1  1  1  1  1  1 ]
[ 1  1  1  0  1  1  1  1  1  1 ]

Output:  
Length of shortest safe route is 13 (Highlighted in Bold)
'''
# Python program to find shortest safe Route in
# the matrix with landmines
import sys

R = 12
C = 10

class Key:
	def __init__(self,i, j):
		self.x = i
		self.y = j

# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [ -1, 0, 0, 1 ]
colNum = [ 0, -1, 1, 0 ]

# A function to check if a given cell (x, y) is
# a valid cell or not
def isValid(x, y):

	if (x < R and y < C and x >= 0 and y >= 0):
		return True

	return False

# A function to mark all adjacent cells of
# landmines as unsafe. Landmines are shown with
# number 0
def findShortestPath(mat):

	for i in range(R):
		for j in range(C):
			# if a landmines is found
			if (mat[i][j] == 0):
				# mark all adjacent cells
				for k in range(4):
					if (isValid(i + rowNum[k], j + colNum[k])):
						mat[i + rowNum[k]][j + colNum[k]] = -1
			
	# mark all found adjacent cells as unsafe
	for i in range(R):
		for j in range(C):
			if (mat[i][j] == -1):
				mat[i][j] = 0

	dist = [[-1 for i in range(C)]for j in range(R)]

	q = []

	for i in range(R):
		if(mat[i][0] == 1):
			q.append(Key(i,0))
			dist[i][0] = 0

	while(len(q) != 0):
		k = q[0]
		q = q[1:]

		d = dist[k.x][k.y]

		x = k.x
		y = k.y

		for k in range(4):
			xp = x + rowNum[k]
			yp = y + colNum[k]
			if(isValid(xp,yp) and dist[xp][yp] == -1 and mat[xp][yp] == 1):
				dist[xp][yp] = d+1
				q.append(Key(xp,yp))
	
	# stores minimum cost of shortest path so far
	ans = sys.maxsize

	# start from first column and take minimum
	for i in range(R):
		if(mat[i][C-1] == 1 and dist[i][C-1] != -1):
			ans = min(ans,dist[i][C-1])

	
	# if destination can be reached
	if(ans == sys.maxsize):
		print("NOT POSSIBLE")
		
	else: # if the destination is not reachable
		print(f"Length of shortest safe route is {ans}")

# Driver code
	
# input matrix with landmines shown with number 0
mat =[
		[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
		[ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
		[ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
		[ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
		[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
		[ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
		[ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
		[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
		[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
		[ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
		[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
		[ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ]
]
	
# find shortest path
findShortestPath(mat)

