'''
Count all possible walks from a source to a destination with exactly k edges
Given a directed graph and two vertices ‘u’ and ‘v’ in it, count all possible walks from ‘u’ to ‘v’ 
with exactly k edges on the walk. 

The graph is given adjacency matrix representation where the value of graph[i][j] 
as 1 indicates that there is an edge from vertex i to vertex j and a value 0 indicates no edge from i to j.

For example, consider the following graph. Let source ‘u’ be vertex 0, destination ‘v’ be 3 and k be 2. 
The output should be 2 as there are two walks from 0 to 3 with exactly 2 edges. The walks are {0, 2, 3} and {0, 1, 3}

Simple Approach: Create a recursive function that takes the current vertex, destination vertex, 
and the count of the vertex. 

Call the recursive function with all adjacent vertices of a current vertex with the value of k as k-1. 
When the value of k is 0, then check whether the current vertex is the destination or not. 

If destination, then the output answer is 1.
'''
# Python3 program to count walks from u to v with exactly k edges

# Number of vertices in the graph
V = 4

# A naive recursive function to count walks from u to v with k edges
def countwalks(graph, u, v, k):

	# Base cases
	if (k == 0 and u == v):
		return 1
	if (k == 1 and graph[u][v]):
		return 1
	if (k <= 0):
		return 0
	
	# Initialize result
	count = 0
	
	# Go to all adjacents of u and recur
	for i in range(0, V):
		
		# Check if is adjacent of u
		if (graph[u][i] == 1): 
			count += countwalks(graph, i, v, k-1)
	
	return count

# Driver Code

# Let us create the graph shown in above diagram
graph = [[0, 1, 1, 1, ],
		[0, 0, 0, 1, ],
		[0, 0, 0, 1, ],
		[0, 0, 0, 0] ]

u = 0; v = 3; k = 2
print(countwalks(graph, u, v, k))

