'''
Smallest Derangement of Sequence

Given the sequence \ S = {1, 2, 3 \dots N}                       
find the lexicographically smallest (earliest in dictionary order) derangement of \ S                    
A derangement of S is any permutation of S such that no two elements in S and its permutation occur at the same position.

Examples:   
Input: 3
Output : 2 3 1
Explanation: The Sequence is 1 2 3.
Possible permutations are (1, 2, 3), (1, 3, 2),
          (2, 1, 3), (2, 3, 1), (3, 1, 2) (3, 2, 1).
Derangements are (2, 3, 1), (3, 1, 2).
Smallest Derangement: (2, 3, 1)

Input : 5
Output : 2 1 4 5 3.
Explanation: Out of all the permutations of 
(1, 2, 3, 4, 5), (2, 1, 4, 5, 3) is the first derangement.
'''
# Efficient Python3 program to find smallest derangement. 

def generate_derangement(N):
	
	# Generate Sequence S 
	S = [0] * (N + 1)
	for i in range(1, N + 1):
		S[i] = i 

	# Generate Derangement 
	D = [0] * (N + 1)
	for i in range(1, N + 1, 2):
		if i == N: 

			# Only if i is odd 
			# Swap S[N-1] and S[N] 
			D[N] = S[N - 1] 
			D[N - 1] = S[N]
		else: 
			D[i] = i + 1
			D[i + 1] = i

	# Print Derangement 
	for i in range(1, N + 1):
		print(D[i], end = " ")
	print()

# Driver Code 
if __name__ == '__main__':
	generate_derangement(10)
	
