'''
Length of Longest Balanced Subsequence
Given a string S, find the length of the longest balanced subsequence in it. A balanced string is defined as:- 

A null string is a balanced string.
If X and Y are balanced strings, then (X)Y and XY are balanced strings.
Examples: 

Input : S = "()())"
Output : 4

()() is the longest balanced subsequence 
of length 4.

Input : s = "()(((((()"
Output : 4
'''
# Python3 program to find length of 
# the longest balanced subsequence 

def maxLength(s, n):
	
	dp = [[0 for i in range(n)]
			for i in range(n)]
			
	# Considering all balanced 
	# substrings of length 2 
	for i in range(n - 1): 
		if (s[i] == '(' and s[i + 1] == ')'): 
			dp[i][i + 1] = 2

	# Considering all other substrings 
	for l in range(2, n):
		i = -1
		for j in range(l, n):
			i += 1
			if (s[i] == '(' and s[j] == ')'): 
				dp[i][j] = 2 + dp[i + 1][j - 1] 
			for k in range(i, j): 
				dp[i][j] = max(dp[i][j], dp[i][k] +
										dp[k + 1][j])
	return dp[0][n - 1] 

# Driver Code 
s = "()(((((()"
n = len(s)
print(maxLength(s, n)) 

