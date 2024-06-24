'''
Given a stream of integers represented as arr[]. 
For each index i from 0 to n-1, print the multiplication of largest, second largest, third largest element 
of the subarray arr[0…i]. If i < 2 print -1. 

Examples: 
Input : arr[] = {1, 2, 3, 4, 5}
Output :-1
        -1
         6
         24
         60
Explanation : for i = 2 only three elements 
are there {1, 2, 3} so answer is 6. For i = 3
largest three elements are {2, 3, 4} their
product is 2*3*4 = 24 ....so on 
'''
# Python3 implementation of largest triplet
# multiplication
from queue import PriorityQueue

# Prints the product of three largest 
# numbers in subarray arr[0..i]
def LargestTripletMultiplication(arr, n):
	
	# Call a priority queue
	q = PriorityQueue()

	# Traversing the array
	for i in range(n): 
		
		# Pushing -arr[i] in array
		# to get max PriorityQueue
		q.put(-arr[i])

		# If less than three elements 
		# are present in array print -1
		if (q.qsize() < 3):
			print(-1)
		else:
			
			# pop three largest elements
			x = q.get()
			y = q.get()
			z = q.get()

			# Reinsert x, y, z in
			# priority_queue
			ans = x * y * z
			
			print(-ans)
			
			q.put(x);
			q.put(y);
			q.put(z);

# Driver Code
if __name__ == '__main__':

	arr = [ 1, 2, 3, 4, 5 ]
	n = len(arr)
	
	LargestTripletMultiplication(arr, n)
	
