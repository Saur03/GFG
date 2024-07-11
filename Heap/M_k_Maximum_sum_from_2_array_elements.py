'''
K maximum sum combinations from two arrays
Given two equally sized arrays (A, B) and N (size of both arrays). 
A sum combination is made by adding one element from array A and another element of array B. Display the maximum K valid sum combinations from all the possible sum combinations. 

Examples: 

Input :  A[] : {3, 2} 
         B[] : {1, 4}
         K : 2 [Number of maximum sum
               combinations to be printed]
Output : 7    // (A : 3) + (B : 4)
         6    // (A : 2) + (B : 4)
Input :  A[] : {4, 2, 5, 1}
         B[] : {8, 0, 3, 5}
         K : 3
Output : 13   // (A : 5) + (B : 8)
         12   // (A : 4) + (B :  8)
         10   // (A : 2) + (B : 8)

'''
import heapq

# Function prints k maximum possible combinations
def KMaxCombinations(a, b, k):
	
	# Sorting the arrays.
	a.sort()
	b.sort()
	
	n = len(a)
	
	# Using a max-heap.
	pq = []
	heapq.heapify(pq)
	pq.append((-a[n-1] - b[n-1], (n - 1, n - 1)))
	
	# Using a set.
	my_set = set() 
	my_set.add((n - 1, n - 1))
	
	
	
	for count in range(K):
		
		# tuple format (sum, (i, j)).
		temp = heapq.heappop(pq)
		
		print(-temp[0])
		
		i = temp[1][0]
		j = temp[1][1]
		sum = a[i - 1] + b[j]
		
		temp1 = (i - 1, j)
		
		# insert (A[i - 1] + B[j], (i - 1, j))
		# into max heap.
		
		# insert only if the pair (i - 1, j) is
		# not already present inside the map i.e.
		# no repeating pair should be present inside
		# the heap.
		if(temp1 not in my_set):
			heapq.heappush(pq, (-sum, temp1))
			my_set.add(temp1)
		
		sum = a[i] + b[j - 1]
		
		temp1 = (i, j - 1)
		
		# insert (A[i1] + B[j = 1], (i, j - 1))
		# into max heap.
		
		# insert only if the pair (i, j - 1)
		# is not present inside the heap.
		if(temp1 not in my_set):
			heapq.heappush(pq, (-sum, temp1))
			my_set.add(temp1)



# Driver Code.
A = [ 1, 4, 2, 3 ];
B = [ 2, 5, 1, 6 ];
K = 4;

# Function call
KMaxCombinations(A, B, K);

