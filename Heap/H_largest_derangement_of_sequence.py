'''
Largest Derangement of a Sequence
Given any sequence, find the largest derangement of .
A derangement D is any permutation of, such that no two elements at the same position in S and D are equal. 
The Largest Derangement is such that.

Examples:  

Input : seq[] = {5, 4, 3, 2, 1}
Output : 4 5 2 1 3

Input : seq[] = {56, 21, 42, 67, 23, 74}
Output : 74, 67, 56, 42, 21, 23
'''
# Python3 program to find the largest derangement
def printLargest(seq, N) :

	res = [0]*N # Stores result

	# Insert all elements into a priority queue
	pq = []
	for i in range(N) :
		pq.append(seq[i]) 

	# Fill Up res[] from left to right
	for i in range(N) : 
		pq.sort()
		pq.reverse()
		d = pq[0]
		del pq[0]
		if (d != seq[i] or i == N - 1) :
			res[i] = d	 
		else :	 

			# New Element popped equals the element 
			# in original sequence. Get the next
			# largest element
			res[i] = pq[0]
			del pq[0]
			pq.append(d)

	# If given sequence is in descending order then 
	# we need to swap last two elements again
	if (res[N - 1] == seq[N - 1]) : 
		res[N - 1] = res[N - 2]
		res[N - 2] = seq[N - 1]
		
	print("Largest Derangement")
	for i in range(N) :
		print(res[i], end = " ")

# Driver code
seq = [ 92, 3, 52, 13, 2, 31, 1 ] 
n = len(seq)
printLargest(seq, n)

