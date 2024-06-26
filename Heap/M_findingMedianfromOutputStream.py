'''
Find Median from Running Data Stream
Given that integers are read from a data stream. 
Find the median of elements read so far in an efficient way. 

There are two cases for median on the basis of data set size.
If the data set has an odd number then the middle one will be consider as median.
If the data set has an even number then there is no distinct middle value 
and the median will be the arithmetic mean of the two middle values.
Example:

Input Data Stream: 5, 15, 1, 3
Output: 5, 10,5, 4
Explanation:
After reading 1st element of stream – 5 -> median = 5
After reading 2nd element of stream – 5, 15 -> median = (5+15)/2 = 10
After reading 3rd element of stream – 5, 15, 1 -> median = 5
After reading 4th element of stream – 5, 15, 1, 3 -> median = (3+5)/2 = 4
'''
# Function to find position to insert current element of stream using binary search

def binarySearch(arr, item, low, high):

	if (low >= high):
		return (low + 1) if (item > arr[low]) else low

	mid = (low + high) // 2

	if (item == arr[mid]):
		return mid + 1

	if (item > arr[mid]):
		return binarySearch(arr, item, mid + 1, high)

	return binarySearch(arr, item, low, mid - 1)

# Function to print median of stream of integers
def printMedian(arr, n):

	i, j, pos, num = 0, 0, 0, 0
	count = 1

	print(f"Median after reading 1 element is {arr[0]}.0")

	for i in range(1, n):
		median = 0
		j = i - 1
		num = arr[i]

		# find position to insert current element in sorted part of array
		pos = binarySearch(arr, num, 0, j)

		# move elements to right to create space to insert the current element
		while (j >= pos):
			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = num

		# increment count of sorted elements in array
		count += 1

		# if odd number of integers are read from stream then middle element in sorted order is median else average of middle elements is median
		if (count % 2 != 0):
			median = arr[count // 2] / 1

		else:
			median = (arr[(count // 2) - 1] + arr[count // 2]) / 2

		print(f"Median after reading {i + 1} elements is {median} ")


# Driver Code
if __name__ == "__main__":

	arr = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
	n = len(arr)

	printMedian(arr, n)

