# Python3 implementation to find the 
# level having Maximum number of Nodes

# Importing Queue
from queue import Queue 

# Helper class that allocates a new 
# node with the given data and None
# left and right pointers. 
class newNode:
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None

# function to find the level 
# having Maximum number of Nodes 
def maxNodeLevel(root):
	if (root == None): 
		return -1

	q = Queue() 
	q.put(root) 

	# Current level 
	level = 0

	# Maximum Nodes at same level 
	Max = -999999999999

	# Level having Maximum Nodes 
	level_no = 0

	while (1):
		
		# Count Nodes in a level 
		NodeCount = q.qsize() 

		if (NodeCount == 0):
			break

		# If it is Maximum till now 
		# Update level_no to current level 
		if (NodeCount > Max):
			Max = NodeCount 
			level_no = level

		# Pop complete current level 
		while (NodeCount > 0):
			Node = q.queue[0] 
			q.get()
			if (Node.left != None):
				q.put(Node.left) 
			if (Node.right != None): 
				q.put(Node.right) 
			NodeCount -= 1

		# Increment for next level 
		level += 1

	return level_no

# Driver Code
if __name__ == '__main__':
	
	# binary tree formation 
	root = newNode(2)	 #	 2	 
	root.left	 = newNode(1)	 #	 / \ 
	root.right	 = newNode(3)	 #	 1	 3	 
	root.left.left = newNode(4)	 # / \ \ 
	root.left.right = newNode(6)	 # 4	 6 8 
	root.right.right = newNode(8) #	 /	 
	root.left.right.left = newNode(5)#	 5	 

	print("Level having Maximum number of Nodes : ", 
								maxNodeLevel(root))

