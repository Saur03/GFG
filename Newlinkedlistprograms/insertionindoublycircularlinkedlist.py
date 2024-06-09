'''
Circular Doubly Linked List has properties of both doubly linked list 
and circular linked list in which two consecutive elements are linked or connected by the previous 
and next pointer and the last node points to the first node by the next pointer 
and also the first node points to the last node by the previous pointer.
'''
class Node:
	def __init__(self):
		# Data in the node
		self.data = None

		# Pointer to the next node
		self.next = None

		# Pointer to the previous node
		self.prev = None
# Function to insert at the end
def insertEnd(value):
	global start

	# If the list is empty, create a
	# single node circular and doubly list
	if (start == None):

		new_node = Node(0)
		new_node.data = value
		new_node.next = new_node.prev = new_node
		start = new_node
		return

	# If list is not empty

	# Find last node */
	last = (start).prev

	# Create Node dynamically
	new_node = Node(0)
	new_node.data = value

	# Start is going to be next of new_node
	new_node.next = start

	# Make new node previous of start
	(start).prev = new_node

	# Make last previous of new node
	new_node.prev = last

	# Make new node next of old last
	last.next = new_node

	# This code is contributed by shivanisinghss2110
