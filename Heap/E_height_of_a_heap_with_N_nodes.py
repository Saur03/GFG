'''
Height of a complete binary tree (or Heap) with N nodes
Consider a Binary Heap of size N. We need to find the height of it.

Examples:  

Input : N = 6
Output : 2
        ()
      /    \
     ()     ()
    /  \    /
  ()    () ()

Input : N = 9
Output : 3
        ()
      /    \
     ()     ()
    /  \    /  \
  ()    () ()   ()
 / \
()  ()
'''
# Python 3 program to find 
# height of complete binary
# tree from total nodes.
import math
def height(N):
	return math.ceil(math.log2(N + 1)) - 1

# driver node
N = 6
print(height(N))

