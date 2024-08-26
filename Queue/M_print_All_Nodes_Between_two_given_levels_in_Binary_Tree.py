'''
Print all nodes between two given levels in Binary Tree.
Given a binary tree, print all nodes between two given levels in a binary tree. 

               1
             /  \
            2    3
           / \  / \
          4   5 6  7 
Print the nodes level-wise, i.e., the nodes for any level should be printed from left to right. 

In the above tree, if the starting level is 2 and the ending level is 3 then the solution should print: 

2 3 
4 5 6 7 
Note: Level number starts with 1. That is, the root node is at level 1.
'''
# Python3 program for Print all nodes between two given levels in a binary tree 

# Helper function that allocates a new node with the given data and None left and right pointers.								 
class newNode: 

	# Construct to create a new node 
	def __init__(self, key): 
		self.data = key
		self.left = None
		self.right = None

# Iterative function to print all nodes between two given levels in a binary tree
def printNodes(root, start, end):
	
	if (root == None): 
		return

	# create an empty queue and
	# enqueue root node
	q = []
	q.append(root)

	# pointer to store current node
	curr = None

	# maintains level of current node
	level = 0

	# run till queue is not empty
	while (len(q)): 
		
		# increment level by 1
		level += 1

		# calculate number of nodes in
		# current level
		size = len(q)

		# process every node of current level
		# and enqueue their non-empty left
		# and right child to queue
		while (size != 0) :
			curr = q[0]
			q.pop(0)

			# print the node if its level is
			# between given levels
			if (level >= start and level <= end) :
				print(curr.data, end = " ")
			
			if (curr.left != None) :
				q.append(curr.left)
			
			if (curr.right != None) :
				q.append(curr.right)
			
			size -= 1
		
		if (level >= start and level <= end) :
			print("")
			
# Driver Code 
if __name__ == '__main__':
	
	""" 
	Let us create Binary Tree shown
	in above example """
	root = newNode(1)
	root.left = newNode(2)

	root.left.left = newNode(4)
	root.left.right = newNode(5)
	root.right = newNode(3)
	root.right.right = newNode(7)
	root.right.left = newNode(6)
	start = 2
	end = 3
	printNodes(root, start, end)
	
