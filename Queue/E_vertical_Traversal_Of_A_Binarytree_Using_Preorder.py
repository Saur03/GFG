'''
Vertical Traversal of a Binary Tree using Preorder.
Given a binary tree, print it vertically. The following examples illustrate the vertical order traversal.

  Input:         1
                  /    \ 
                2      3
               / \   /   \
             4   5  6   7
                         /  \ 
                       8    9 

Output: 

4
2
1 5 6
3 8
7
9

print-binary-tree-in-vertical-order
'''
class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def get_order(root, hd, m, min_hd, max_hd):
    if root is None:
        return

    # Store current node in map 'm'
    if hd not in m:
        m[hd] = []
    m[hd].append(root.key)

    min_hd[0] = min(min_hd[0], hd)
    max_hd[0] = max(max_hd[0], hd)

    # Store nodes in left subtree
    get_order(root.left, hd - 1, m, min_hd, max_hd)

    # Store nodes in right subtree
    get_order(root.right, hd + 1, m, min_hd, max_hd)

def print_order(root):
    # Create a map and store vertical order
    # in map using function get_order()
    m = {}
    min_hd = [0]
    max_hd = [0]

    get_order(root, 0, m, min_hd, max_hd)

    # Traverse through all horizontal 
    # distances from smallest to 
    # largest and print nodes at every
    # distance
    for d in range(min_hd[0], max_hd[0] + 1):
        print(" ".join(map(str, m[d])))

# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)
    print_order(root)
