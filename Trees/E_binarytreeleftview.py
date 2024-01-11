'''
Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. 
The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   

Example 1:

Input:
   1
 /  \
3    2
Output: 1 3
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    if not root:
        return []
    
    q = []
    q.append(root)

    while len(q):
        n = len(q)

        for i in range(1, n+1):
            temp = q[0]
            q.pop(0)

            if i == 1:
                print(temp.data, end = " ")

            if temp.left != None:
                q.append(temp.left)

            if temp.right != None:
                q.append(temp.right)    

    return q            