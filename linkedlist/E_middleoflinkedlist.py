'''
Find the middle of a given linked list
For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 
'''
# To find the middle of a given linked list, you can use the "two-pointer" approach, also known as the "slow and fast" pointers method. This technique involves using two pointers: one moving at half the speed of the other. When the faster pointer reaches the end of the linked list, the slower pointer will be pointing at the middle node.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle(head):
    if not head:
        return None
    
    slow_pointer = head
    fast_pointer = head
    
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        
    return slow_pointer        

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle_node = find_middle(head)
if middle_node:
    print("Middle node value:", middle_node.value)
else:
    print("Linked list is empty.")    