'''
Given an array representation of min Heap, convert it to max Heap.

Examples: 

Input: arr[] = {3, 5, 9, 6, 8, 20, 10, 12, 18, 9}

               3
            /     \
          5       9
        /   \    /  \
      6     8  20   10
    /  \   /
12   18 9 

Output: arr[] = {20, 18, 10, 12, 9, 9, 3, 5, 6, 8}

           20
         /    \
      18      10
     /    \    /  \
  12     9  9    3
 /  \   /
5    6 8 

Input: arr[] = {3, 4, 8, 11, 13}
Output:  arr[] = {13, 11, 8, 4, 3}
'''
# A Python3 program to convert min Heap to max Heap

# to heapify a subtree with root at given index
def MaxHeapify(arr, i, N):
	l = 2 * i + 1
	r = 2 * i + 2
	largest = i
	if l < N and arr[l] > arr[i]:
		largest = l
	if r < N and arr[r] > arr[largest]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		MaxHeapify(arr, largest, N)

# This function basically builds max heap
def convertMaxHeap(arr, N):

	# Start from bottommost and rightmost
	# internal node and heapify all
	# internal nodes in bottom up way
	for i in range(int((N - 2) / 2), -1, -1):
		MaxHeapify(arr, i, N)

# A utility function to print a given array of given size

def printArray(arr, size):
	for i in range(size):
		print(arr[i], end=" ")
	print()


# Driver Code
if __name__ == '__main__':

	# array representing Min Heap
	arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
	N = len(arr)

	print("Min Heap array : ")
	printArray(arr, N)

	# Function call
	convertMaxHeap(arr, N)

	print("Max Heap array : ")
	printArray(arr, N)

