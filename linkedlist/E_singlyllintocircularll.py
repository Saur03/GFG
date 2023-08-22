'''
Convert singly linked list into circular linked list
'''
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
def convert_to_circular_linked_list(head):
    if not head:
        return None        
    
    current = head
    while current.next is not None:
        current = current.next
        
    current.next = head
    
    return head


# Create a singly linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Convert to circular linked list
circular_head = convert_to_circular_linked_list(head)

# Printing the circular linked list to verify

current = circular_head
for _ in range(10):# Printing a few times to verify circular structure  
    print(current.value, end=" -> ")  
    current = current.next   
print("...")  # To show that it's circular    