'''
Print all nodes less than a value x in a Min Heap.

Given a binary min heap and a value x, print all the binary heap nodes having value less than the given value x.

Examples : Consider the below min heap as
        common input two both below examples.
                   2
                /     \
               3        15
            /    \     / \
           5       4  45  80
          / \     / \
         6   150 77 120

Input  : x = 15        
Output : 2 3 5 6 4

Input  : x = 80
Output : 2 3 5 6 4 77 15 45
'''
# A Python program to print all values smaller than a given value in Binary  Heap

# A class for Min Heap
class MinHeap:
	# pointer to array of elements in heap
	harr = []

	# maximum possible size of min heap
	capacity = 0
	heap_size = 0 # Current no. of elements.

	# Constructor
	def __init__(self, capacity):
		self.heap_size = 0
		self.capacity = capacity
		self.harr = [0] * capacity

	# to heapify a subtree with root at
	# given index
	def MinHeapify(self, i):
		l = self.left(i)
		r = self.right(i)
		smallest = i
		if l < self.heap_size and self.harr[l] < self.harr[i]:
			smallest = l
		if r < self.heap_size and self.harr[r] < self.harr[smallest]:
			smallest = r
		if smallest != i:
			self.harr[i], self.harr[smallest] = self.harr[smallest], self.harr[i]
			self.MinHeapify(smallest)

	def parent(self, i):
		return (i - 1) // 2

	def left(self, i):
		return (2 * i + 1)

	def right(self, i):
		return (2 * i + 2)

	# Inserts a new key 'k'
	def insertKey(self, k):
		if self.heap_size == self.capacity:
			print("\nOverflow: Could not insertKey\n")
			return
		# First insert the new key at the end
		self.heap_size += 1
		i = self.heap_size - 1
		self.harr[i] = k
		# Fix the min heap property if it is violated
		while i != 0 and self.harr[self.parent(i)] > self.harr[i]:
			self.harr[i], self.harr[self.parent(i)] = self.harr[self.parent(i)], self.harr[i]
			i = self.parent(i)

	# Function to print all nodes smaller than k
	def printSmallerThan(self, x, pos=0):
		"""
		Make sure item exists
		"""
		if pos >= self.heap_size:
			return
		if self.harr[pos] >= x:
			"""
			Skip this node and its descendants,
			as they are all >= x .
			"""
			return
		print(self.harr[pos], end=" ")
		self.printSmallerThan(x, self.left(pos))
		self.printSmallerThan(x, self.right(pos))


# Driver program to test above functions
def main():
	h = MinHeap(50)
	h.insertKey(3)
	h.insertKey(2)
	h.insertKey(15)
	h.insertKey(5)
	h.insertKey(4)
	h.insertKey(45)
	h.insertKey(80)
	h.insertKey(6)
	h.insertKey(150)
	h.insertKey(77)
	h.insertKey(120)

	# Print all nodes smaller than 100.
	x = 100
	h.printSmallerThan(x)

if __name__ == "__main__":
	main()

