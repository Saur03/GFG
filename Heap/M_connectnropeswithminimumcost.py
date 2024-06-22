'''
Given are N ropes of different lengths, the task is to connect these ropes into one rope with minimum cost, such that the cost to connect two ropes is equal to the sum of their lengths.

Examples:

Input: arr[] = {4,3,2,6} , N = 4
Output: 29
Explanation: 

First, connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6, and 5. 
Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9. 
Finally connect the two ropes and all ropes have connected.
'''
# Python3 program to connect n ropes with minimum cost
import heapq

def minCost(arr, n):

	# Create a priority queue out of the given list
	heapq.heapify(arr)

	# Initialize result
	res = 0

	# While size of priority queue is more than 1
	while(len(arr) > 1):

		# Extract shortest two ropes from arr
		first = heapq.heappop(arr)
		second = heapq.heappop(arr)

		# Connect the ropes: update result and insert the new rope to arr
		res += first + second
		heapq.heappush(arr, first + second)

	return res


# Driver code
if __name__ == '__main__':

	lengths = [4, 3, 2, 6]
	size = len(lengths)

	print("Total cost for connecting ropes is " +
		str(minCost(lengths, size)))

