'''
Check whether a given graph is Bipartite or not.
A Bipartite Graph is a graph whose vertices can be divided into two independent sets, 
U and V such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U. 
In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U. 
We can also say that there is no edge that connects vertices of same set.

A bipartite graph is possible if the graph coloring is possible using two colors 
such that vertices in a set are colored with the same color. 

Note that it is possible to color a cycle graph with even cycle using two colors. For example, see the following graph. 

'''

# Python3 program to find out whether a given 
# graph is Bipartite or not using recursion. 
V = 4

def colorGraph(G, color, pos, c): 
	
	if color[pos] != -1 and color[pos] != c: 
		return False
		
	# color this pos as c and all its neighbours and 1-c 
	color[pos] = c 
	ans = True
	for i in range(0, V): 
		if G[pos][i]: 
			if color[i] == -1: 
				ans &= colorGraph(G, color, i, 1-c) 
				
			if color[i] !=-1 and color[i] != 1-c: 
				return False
		
		if not ans: 
			return False
	
	return True

def isBipartite(G): 
	
	color = [-1] * V 
		
	#start is vertex 0 
	pos = 0
	# two colors 1 and 0 
	return colorGraph(G, color, pos, 1) 

if __name__ == "__main__": 

	G = [[0, 1, 0, 1], 
		[1, 0, 1, 0], 
		[0, 1, 0, 1], 
		[1, 0, 1, 0]] 
	
	if isBipartite(G): print("Yes") 
	else: print("No") 

