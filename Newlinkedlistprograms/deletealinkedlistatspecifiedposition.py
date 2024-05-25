'''
In this method, we will remove the node at the given index, 
this method is similar to the insert_at_inded() method. 
In this method, if the head is None we simply return else we initialize a current_node with self.head and position with 0. 
If the position is equal to the index we called the remove_first_node() method 
else we traverse to the one node before that we want to remove using the while loop. 
After that when we out of the while loop we check that current_node is equal to None if not 
then we make the next of current_node equal to the next of node 
that we want to remove else we print the message “Index not present” because current_node is equal to None.
'''
# Method to remove at given index
def remove_at_index(self, index):
		if self.head == None:
			return

		current_node = self.head
		position = 0
		if position == index:
			self.remove_first_node()
		else:
			while(current_node != None and position+1 != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:
				current_node.next = current_node.next.next
			else:
				print("Index not present")
