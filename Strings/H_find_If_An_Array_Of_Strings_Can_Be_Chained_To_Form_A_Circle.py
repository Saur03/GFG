'''
Find if an array of strings can be chained to form a circle | Set 2.
Given an array of strings, find if the given strings can be chained to form a circle. A string X can be put before another string Y in a circle if the last character of X is the same as the first character of Y.

Examples: 

Input: arr[] = {"geek", "king"}
Output: Yes, the given strings can be chained.
Note that the last character of first string is same
as first character of second string and vice versa is
also true.

Input: arr[] = {"for", "geek", "rig", "kaf"}
Output: Yes, the given strings can be chained.
The strings can be chained as "for", "rig", "geek" 
and "kaf"

Input: arr[] = {"aab", "bac", "aaa", "cda"}
Output: Yes, the given strings can be chained.
The strings can be chained as "aaa", "aab", "bac" 
and "cda"

Input: arr[] = {"aaa", "bbb", "baa", "aab"};
Output: Yes, the given strings can be chained.
The strings can be chained as "aaa", "aab", "bbb" 
and "baa"

Input: arr[] = {"aaa"};
Output: Yes

Input: arr[] = {"aaa", "bbb"};
Output: No

Input  : arr[] = ["abc", "efg", "cde", "ghi", "ija"]
Output : Yes
These strings can be reordered as, “abc”, “cde”, “efg”,
“ghi”, “ija”

Input : arr[] = [“ijk”, “kji”, “abc”, “cba”]
Output : No
'''
# Python3 code to check if 
# cyclic order is possible 
# among strings under given 
# constraints 
M = 26

# Utility method for a depth 
# first search among vertices 
def dfs(g, u, visit): 
	visit[u] = True

	for i in range(len(g[u])): 
		if(not visit[g[u][i]]): 
			dfs(g, g[u][i], visit) 

# Returns true if all vertices 
# are strongly connected i.e. 
# can be made as loop 
def isConnected(g, mark, s): 

	# Initialize all vertices 
	# as not visited 
	visit = [False for i in range(M)] 

	# Perform a dfs from s 
	dfs(g, s, visit) 

	# Now loop through 
	# all characters 
	for i in range(M): 

		# I character is marked 
		# (i.e. it was first or last 
		# character of some string) 
		# then it should be visited 
		# in last dfs (as for looping, 
		# graph should be strongly 
		# connected) */ 
		if(mark[i] and (not visit[i])): 
			return False
			
	# If we reach that means 
	# graph is connected 
	return True

# return true if an order among 
# strings is possible 
def possibleOrderAmongString(arr, N): 

	# Create an empty graph 
	g = {} 

	# Initialize all vertices 
	# as not marked 
	mark = [False for i in range(M)] 

	# Initialize indegree and 
	# outdegree of every 
	# vertex as 0. 
	In = [0 for i in range(M)] 
	out = [0 for i in range(M)] 

	# Process all strings 
	# one by one 
	for i in range(N): 

		# Find first and last 
		# characters 
		f = (ord(arr[i][0]) -
			ord('a')) 
		l = (ord(arr[i][-1]) -
			ord('a')) 

		# Mark the characters 
		mark[f] = True
		mark[l] = True

		# Increase indegree 
		# and outdegree count 
		In[l] += 1
		out[f] += 1

		if f not in g: 
			g[f] = [] 

		# Add an edge in graph 
		g[f].append(l) 

	# If for any character 
	# indegree is not equal to 
	# outdegree then ordering 
	# is not possible 
	for i in range(M): 
		if(In[i] != out[i]): 
			return False
			
	return isConnected(g, mark, 
					ord(arr[0][0]) -
					ord('a')) 

# Driver code 
arr = ["ab", "bc", 
	"cd", "de", 
	"ed", "da"] 
N = len(arr) 
if(possibleOrderAmongString(arr, N) ==
False): 
	print("Ordering not possible") 
else: 
	print("Ordering is possible") 

