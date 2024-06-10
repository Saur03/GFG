'''
Insertion at the beginning of the list: 
To insert a node at the beginning of the list, 
create a node(Say T) with data = 5, T next pointer points to the first node of the list, 
T previous pointer points to the last node of the list, 
last node’s next pointer points to this T node, first node’s previous pointer 
also points this T node and at last don’t forget to shift ‘Start’ pointer to this T node.
'''
class Node:
	def __init__(self):
		# Data in the node
		self.data = None

		# Pointer to the next node
		self.next = None

		# Pointer to the previous node
		self.prev = None

# Function to insert Node at the beginning
# of the List,


def insertBegin(value):
	global start

	# Pointer points to last Node
	last = (start).prev

	new_node = Node(0)
	new_node.data = value # Inserting the data

	# setting up previous and
	# next of new node
	new_node.next = start
	new_node.prev = last

	# Update next and previous pointers
	# of start and last.
	last.next = (start).prev = new_node

	# Update start pointer
	start = new_node

	# This code is contributed by shivanisinghss2110
