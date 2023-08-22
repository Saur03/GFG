'''
Exchange first and last nodes in Circular Linked List
Input : 5 4 3 2 1
Output : 1 4 3 2 5

Input  : 6 1 2 3 4 5 6 7 8 9
Output : 9 1 2 3 4 5 6 7 8 6
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
        
def addToEmpty(head, data):
    # This function is only for empty list
    if (head != None):
        return head
    # Creating a node dynamically.
    temp = Node(data)
    # Assigning the data.
    temp.data = data
    head = temp
    # Creating the link.
    head.next = head
    return head

def addBegin(head, data):
    if (head == None):
        return addToEmpty(head, data)
    temp = Node(data)
    temp.data = data
    temp.next = head.next
    head.next = temp
    
    return head

# function for traversing the list

def traverse(head):
    
    if (head == None):
        print("List is empty.")
        return
    # Pointing to first Node of the list.
    p = head
    print(p.data, end=" ")
    p = p.next
    
    # Traversing the list.
    while(p != head):
        
        print(p.data, end=" ")
        p = p.next
        
def exchangeNodes(head):
    # Cases Handled: Linked List either empty or containing single node.
    if head == None or head.next == head:
        return head
    # Cases Handled: Linked List containing only two nodes
    elif head.next.next == head:
        head = head.next
        return head
    # Cases Handled: Linked List containing multiple nodes
    else:
        prev = None
        curr = head
        temp = head
        # finding last and second last nodes in linkedlist list
        while curr.next != head:
            prev = curr
            curr = curr.next        
        # point the last node to second node of the list    
        curr.next = temp.next
        # point the second last node to first node
        prev.next = temp
        # point the end of node to start ( make linked list circular )
        temp.next = curr
        # mark the starting of linked list
        head = curr
        
        return head   
    
    
if __name__ == '__main__':
    
    head = None
    head = addToEmpty(head, 6)
    for x in range(5, 0, -1):
        head = addBegin(head, x)
    print("List Before: ", end="")
    traverse(head)
    print()
    
    print("List After: ", end="")
    head = exchangeNodes(head)
    traverse(head)         
            