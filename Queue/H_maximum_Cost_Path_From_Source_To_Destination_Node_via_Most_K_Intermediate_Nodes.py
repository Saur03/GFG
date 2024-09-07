'''
Maximum cost path from source node to destination node via at most K intermediate nodes

Given a directed weighted graph consisting of N vertices and an array Edges[][], 
with each row representing two vertices connected by an edge and the weight of that edge, 
the task is to find the path with the maximum sum of weights from a given source vertex src 
to a given destination vertex dst, made up of at most K intermediate vertices. 

If no such path exists, then print -1.

Examples:

Input: N = 3, Edges[][] = {{0, 1, 100}, {1, 2, 100}, {0, 2, 500}}, src = 0, dst = 2, K = 0
Output: 500
Explanation:
Path 0 → 2: The path with maximum weight and at most 0 intermediate nodes is of weight 500.
'''
# Python3 program for the above approach
from collections import deque

# Function to find the longest distance
# from source to destination with at
# most K intermediate nodes
def findShortestPath(n, edges, src, dst, K):
	
	# Initialize the adjacency list
	adjlist = [[] for i in range(n)]
	
	# Initialize a queue to perform BFS
	q = deque()

	mp = {}

	# Store the maximum distance of
	# every node from source vertex
	ans = -10**9

	# Initialize adjacency list
	for i in range(len(edges)):
		edge = edges[i]
		adjlist[edge[0]].append([edge[1], 
								edge[2]])

	# Push the first element into queue
	q.append([src, 0])

	level = 0

	# Iterate until the queue becomes empty
	# and the number of nodes between src
	# and dst vertex is at most to K
	while (len(q) > 0 and level < K + 2):

		# Current size of the queue
		sz = len(q)

		for i in range(sz):
			
			# Extract the front
			# element of the queue
			pr = q.popleft()
			
			# Pop the front element
			# of the queue
			# q.pop()

			# If the dst vertex is reached
			if (pr[0] == dst):
				ans = max(ans, pr[1])

			# Traverse the adjacent nodes
			for pr2 in adjlist[pr[0]]:
				
				# If the distance is greater
				# than the current distance
				if ((pr2[0] not in mp) or
				mp[pr2[0]] > pr[1] + pr2[1]):
					
					# Push it into the queue
					q.append([pr2[0], pr[1] + pr2[1]])
					mp[pr2[0]] = pr[1] + pr2[1]

		# Increment the level by 1
		level += 1

	# Finally, return the maximum distance
	return ans if ans != -10**9 else -1

# Driver Code
if __name__ == '__main__':
	
	n, src, dst, k = 3, 0, 2, 1

	edges= [ [ 0, 1, 100 ],
			[ 1, 2, 100 ],
			[ 0, 2, 500 ] ]

	print(findShortestPath(n, edges,src, dst, k))

