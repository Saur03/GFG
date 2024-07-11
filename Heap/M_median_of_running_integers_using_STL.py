'''
Median of Stream of Running Integers using STL
Given that integers are being read from a data stream. 
Find the median of all the elements read so far starting from the first integer till the last integer. 
This is also called the Median of Running Integers. 
The data stream can be any source of data, for example, a file, an array of integers, input stream etc.
'''
# python3 program to find med in stream of running integers
from heapq import *

# function to calculate med of stream
def printMedians(arr, n):
	# max heap to store the smaller half elements
	s = []
	# min heap to store the greater half elements
	g = []

	heapify(s)
	heapify(g)

	med = arr[0]
	heappush(s, arr[0])

	print(med)

	# reading elements of stream one by one
	for i in range(1, n):
		x = arr[i]

		# case1(left side heap has more elements)
		if len(s) > len(g):
			if x < med:
				heappush(g, heappop(s))
				heappush(s, x)
			else:
				heappush(g, x)
			med = (nlargest(1, s)[0] + nsmallest(1, g)[0])/2

		# case2(both heaps are balanced)
		elif len(s) == len(g):
			if x < med:
				heappush(s, x)
				med = nlargest(1, s)[0]
			else:
				heappush(g, x)
				med = nsmallest(1, g)[0]

		# case3(right side heap has more elements)
		else:
			if x > med:
				heappush(s, heappop(g))
				heappush(g, x)
			else:
				heappush(s, x)
			med = (nlargest(1, s)[0] + nsmallest(1, g)[0])/2

		print(med)

# Driver program to test above functions
arr = [5, 15, 10, 20, 3]
printMedians(arr, len(arr))

