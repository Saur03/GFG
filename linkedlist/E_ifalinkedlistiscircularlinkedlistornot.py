'''
Check if a linked list is Circular Linked List
# To check if a linked list is a circular linked list in Python, you can use the "tortoise and hare" approach, also known as the "Floyd's cycle detection algorithm." This algorithm involves using two pointers, one moving at a slower pace and another moving at a faster pace. If the linked list is circular, the faster pointer will eventually catch up to the slower pointer, indicating the presence of a cycle.
'''
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
def is_circular_linked_list(head):
    if not head:
        return False
    
    slow_pointer = head
    fast_pointer = head
    
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        
        if slow_pointer == fast_pointer:
            return True
        
    return False


# Create a circular linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 2 (points back to 2)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next  # Creating the cycle

is_circular = is_circular_linked_list(head)
if is_circular:
    print("The linked list is circular.")    
else:
    print("The linked list is not circular.")            