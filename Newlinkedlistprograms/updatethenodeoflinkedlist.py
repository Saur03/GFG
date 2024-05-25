'''
Update the Node of a Linked List

This code defines a method called updateNode in a linked list class.
It is used to update the value of a node at a given position in the linked list.
'''
# Update node of a linked list at given position
def updateNode(self, val, index):
	current_node = self.head
	position = 0
	if position == index:
		current_node.data = val
	else:
		while(current_node != None and position != index):
			position = position+1
			current_node = current_node.next

		if current_node != None:
			current_node.data = val
		else:
			print("Index not present")
