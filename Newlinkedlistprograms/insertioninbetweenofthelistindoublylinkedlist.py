'''
To insert a node in between the list, two data values are required one after 
which new node will be inserted and another is the data of the new node.
'''
class Node:
	def __init__(self):
		# Data in the node
		self.data = None

		# Pointer to the next node
		self.next = None

		# Pointer to the previous node
		self.prev = None

# Function to insert node with value as value1.
# The new node is inserted after the node with
# with value2


def insertAfter(value1, value2):
	global start
	new_node = Node(0)
	new_node.data = value1 # Inserting the data

	# Find node having value2 and
	# next node of it
	temp = start
	while (temp.data != value2):
		temp = temp.next
	next = temp.next

	# insert new_node between temp and next.
	temp.next = new_node
	new_node.prev = temp
	new_node.next = next
	next.prev = new_node

# this code is contributed by shivanisinghss2110
