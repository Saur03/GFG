'''
Write a function that counts the number of times a given int occurs in a Linked List
Given a singly linked list and a key, count the number of occurrences of the given key in the linked list. For example, if the given linked list is 1->2->1->2->1->3->1 and the given key is 1, then the output should be 4.
'''
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
  
def count_occurrences(head, target):
    count = 0
    current = head
    
    while current is not None:
        if current.value == target:
            count += 1
            
        current = current.next 
        
    return count

# Create a linked list: 1 -> 2 -> 3 -> 2 -> 4 -> 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(2)

target_value = 2
occurrences = count_occurrences(head, target_value)
print(f"The value {target_value} occurs {occurrences} times in the linked list.")           
