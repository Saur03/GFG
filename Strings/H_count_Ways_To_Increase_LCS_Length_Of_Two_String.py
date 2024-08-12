'''
Count ways to increase LCS length of two strings by one.
Given two strings of lower alphabet characters, we need to find the number of ways to insert a character in the first string such that length of LCS of both strings increases by one. 

Examples:  

Input : str1 = “abab”, str2 = “abc”
Output : 3
LCS length of given two strings is 2.
There are 3 ways of insertion in str1, 
to increase the LCS length by one which 
are enumerated below, 
str1 = “abcab”    str2 = “abc”  LCS length = 3
str1 = “abacb”    str2 = “abc”  LCS length = 3
str1 = “ababc”    str2 = “abc”  LCS length = 3

Input : str1 = “abcabc”, str2 = “abcd”
Output : 4
'''
# Python3 program to get number of ways to increase
# LCS by 1

M = 26

# Method returns total ways to increase LCS length by 1
def waysToIncreaseLCSBy1(str1, str2):
	m = len(str1)
	n = len(str2)

	# Fill positions of each character in vector
	# vector<int> position[M];
	position = [[] for i in range(M)]
	for i in range(1, n+1, 1):
		position[ord(str2[i-1])-97].append(i)

	# Initializing 2D array by 0 values
	lcsl = [[0 for i in range(n+2)] for j in range(m+2)]
	lcsr = [[0 for i in range(n+2)] for j in range(m+2)]

	# Filling LCS array for prefix substrings
	for i in range(1, m+1, 1):
		for j in range(1, n+1,1):
			if (str1[i-1] == str2[j-1]):
				lcsl[i][j] = 1 + lcsl[i-1][j-1]
			else:
				lcsl[i][j] = max(lcsl[i-1][j],
								lcsl[i][j-1])

	# Filling LCS array for suffix substrings
	for i in range(m, 0, -1):
		for j in range(n, 0, -1):
			if (str1[i-1] == str2[j-1]):
				lcsr[i][j] = 1 + lcsr[i+1][j+1]
			else:
				lcsr[i][j] = max(lcsr[i+1][j],
								lcsr[i][j+1])

		# Looping for all possible insertion positions
		# in first string
	ways = 0
	for i in range(0, m+1,1):
		# Trying all possible lower case characters
		for C in range(0, 26,1):
			# Now for each character, loop over same
			# character positions in second string
			for j in range(0, len(position[C]),1):
				p = position[C][j]

				# If both, left and right substrings make
				# total LCS then increase result by 1
				if (lcsl[i][p-1] + lcsr[i+1][p+1] == lcsl[m][n]):
					ways += 1
	return ways


# Driver code to test above methods
str1 = "abcabc"
str2 = "abcd"
print(waysToIncreaseLCSBy1(str1, str2))

