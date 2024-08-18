'''
Print Right View of a Binary Tree.
Given a Binary Tree, print the Right view of it. 

The right view of a Binary Tree is a set of nodes visible when the tree is visited from the Right side.

Examples: 

Input:
          1
       /     \
     2        3
   /   \       /  \
  4     5   6    7
                 \
                   8
Output: Right view of the tree is 1 3 7 8

Input:
          1
       /     
     8        
   / 
  7
Output: Right view of the tree is 1 8 7
'''
# Python code to implement the morris traversal approach

# Definition for a binary tree node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rightSideView(root):
    res = []
    curr = root
    while curr:
        if not curr.right:  # if there is no right child,
                            # add the current node's value
                            # to the vector
            res.append(curr.val)
            curr = curr.right  # move to the right child
        else:  # if there is a right child
            next = curr.right  # set the next node to the
            # right child
            while next.left and next.left != curr:
                # traverse the left subtree of the right
                # child untill a leaf node or the current
                # node is reached
                next = next.left

            if not next.left:  # if the left child of the
                              # next node is NULL
                res.append(curr.val)
                next.left = curr
                curr = curr.right
            else:
                next.left = None
                curr = curr.left
    return res


# Driver code
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    res = rightSideView(root)
    for i in res:
        print(i, end=" ")
    print()
