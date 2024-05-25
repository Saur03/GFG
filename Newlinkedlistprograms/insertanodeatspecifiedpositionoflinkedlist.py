'''
Insert a Node at a Specific Position in a Linked List:-

This method inserts the node at the given index in the linked list. 
In this method, we create a new_node with given data , a current_node that equals to the head, 
and a counter ‘position’ initializes with 0. 
Now, if the index is equal to zero it means the node is to be inserted at begin so we called insertAtBegin() method 
else we run a while loop until the current_node is not equal to None 
or (position+1) is not equal to the index 
we have to at the one position back to insert at a given position to make the linking of nodes and in each iteration, 
we increment the position by 1 and make the current_node next of it. 
When the loop breaks and if current_node is not equal to None we insert new_node at after to the current_node. 
If current_node is equal to None it means that the index is not present in the list and we print “Index not present”.
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
# Indexing starts from 0.
def insertAtIndex(self, data, index):
		new_node = Node(data)
		current_node = self.head
		position = 0
		if position == index:
			self.insertAtBegin(data)
		else:
			while(current_node != None and position+1 != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:

				new_node.next = current_node.next
				current_node.next = new_node
			else:
				print("Index not present")
