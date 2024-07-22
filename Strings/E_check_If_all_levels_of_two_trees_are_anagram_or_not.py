'''
Check if all levels of two trees are anagrams or not.

Given two binary trees, we have to check if each of their levels is an anagram of the other or not. 
Example: 

Tree 1:
Level 0 : 1
Level 1 : 3, 2
Level 2 : 5, 4

Tree 2:
Level 0 : 1
Level 1 : 2, 3
Level 2 : 4, 5
'''
# A Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Returns true if trees with root1 and root2 are level by level anagram, else returns false.
def areAnagrams(root1, root2):
    # Base Cases
    if (root1 == None and root2 == None):
        return True
    if (root1 == None or root2 == None):
        return False

    # start level order traversal of two trees using two queues.
    q1 = []
    q2 = []
    q1.append(root1)
    q2.append(root2)

    # Hashmap to store the elements that occur in each level.
    m = {}

    while (len(q1) > 0 and len(q2) > 0):
        # n1 (queue size) indicates number of Nodes at current level in first tree and n2 indicates number of nodes in current level of second tree.
        n1 = len(q1)
        n2 = len(q2)

        # If n1 and n2 are different
        if (n1 != n2):
            return False

        # If level order traversal is over
        if (n1 == 0):
            break

        # Dequeue all Nodes of current level and
        # Enqueue all Nodes of next level
        while (n1 > 0):
            node1 = q1.pop(0)

            # Insert element into hashmap
            m[node1.data] = m.get(node1.data, 0) + 1

            # Insert left and right nodes into queue if
            # exists.
            if (node1.left != None):
                q1.append(node1.left)
            if (node1.right != None):
                q1.append(node1.right)
            n1 -= 1

        while (n2 > 0):
            node2 = q2.pop(0)

            # if element from second tree isn't present in
            # the first tree of same level then it can't be
            # an anagram.
            if (m.get(node2.data, 0) == 0):
                return False

            # Reduce frequency of element if present else
            # adds it element to hash map with negative
            # frequency.
            m[node2.data] = m.get(node2.data, 0) - 1

            # If frequency of the element becomes zero then
            # remove the element from hashmap.
            if (m[node2.data] == 0):
                m.pop(node2.data)

            # Insert left and right nodes into queue if
            # exists.
            if (node2.left != None):
                q2.append(node2.left)
            if (node2.right != None):
                q2.append(node2.right)
            n2 -= 1

        # If nodes of current levels are anagrams the
        # hashmap wouldn't contain any elements.
        if (len(m) > 0):
            return False

    if(len(q1) == 0 and len(q2) == 0):
        return True
    return False

# Utility function to create a new tree Node


def newNode(data):
    temp = Node(data)
    temp.left = None
    temp.right = None
    return temp


# Driver program to test above functions
if __name__ == '__main__':

    # Constructing both the trees.
    root1 = newNode(1)
    root1.left = newNode(3)
    root1.right = newNode(2)
    root1.right.left = newNode(5)
    root1.right.right = newNode(4)

    root2 = newNode(1)
    root2.left = newNode(2)
    root2.right = newNode(3)
    root2.left.left = newNode(4)
    root2.left.right = newNode(5)

    if (areAnagrams(root1, root2)):
        print("Yes")
    else:
        print("No")

