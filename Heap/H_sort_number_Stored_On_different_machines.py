'''
Sort numbers stored on different machines
Given N machines. Each machine contains some numbers in sorted form. 
But the amount of numbers, each machine has is not fixed. 
Output the numbers from all the machine in sorted non-decreasing form. 
Example:

Machine M1 contains 3 numbers: {30, 40, 50}
Machine M2 contains 2 numbers: {35, 45} 
Machine M3 contains 5 numbers: {10, 60, 70, 80, 100}
Output: {10, 30, 35, 40, 45, 50, 60, 70, 80, 100}
'''
# A program to take numbers from different machines and print them in sorted order

# A Linked List node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# A Min Heao (Collection of Min Heap nodes)
class MinHeap:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity
        self.array = []

# A utility function to insert a new node at the beginning of linked list
def push(head_ref, new_data):
    new_node = ListNode(new_data)
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

# A utility function to swap two min heap nodes. This function
# is needed in minHeapify
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# The standard minHeapify function.
def min_heapify(min_heap, idx):
    left = 2 * idx + 1
    right = 2 * idx + 2
    smallest = idx

    if (left < min_heap.count and
            min_heap.array[left][0].val < min_heap.array[smallest][0].val):
        smallest = left
    if (right < min_heap.count and
            min_heap.array[right][0].val < min_heap.array[smallest][0].val):
        smallest = right
    if smallest != idx:
        min_heap.array[smallest], min_heap.array[idx] = swap(
            min_heap.array[smallest], min_heap.array[idx])
        min_heapify(min_heap, smallest)

# A utility function to check whether a Min Heap is empty or not


def is_empty(min_heap):
    return min_heap.count == 0

# A standard function to build a heap
def build_min_heap(min_heap):
    n = min_heap.count - 1
    for i in range((n - 1) // 2, -1, -1):
        min_heapify(min_heap, i)

# This function inserts array elements to heap and then calls
# buildHeap for heap property among nodes
def populate_min_heap(min_heap, array, n):
    for i in range(n):
        min_heap.array.append((array[i], i))
        min_heap.count += 1
    build_min_heap(min_heap)

# Return minimum element from all linked lists
def extract_min(min_heap):
    if is_empty(min_heap):
        return None
    temp = min_heap.array[0][0]

    if temp.next is not None:
        min_heap.array[0] = (temp.next, min_heap.array[0][1])
    else:
        min_heap.array[0] = min_heap.array[min_heap.count - 1]
        min_heap.count -= 1

    min_heapify(min_heap, 0)
    return temp

# The main function that takes an array of lists from N machines
# and generates the sorted output
def external_sort(array, n):
     # Create a min heap of size equal to number of machines
    min_heap = MinHeap(n)

    populate_min_heap(min_heap, array, n)

    while not is_empty(min_heap):
        temp = extract_min(min_heap)
        print(temp.val, end=" ")


# Driver program to test above functions
if __name__ == '__main__':
    N = 3  # Number of machines
    array = [None] * N

    # an array of pointers storing the head nodes of the linked lists
    array[0] = None
    array[0] = push(array[0], 50)
    array[0] = push(array[0], 40)
    array[0] = push(array[0], 30)

    # Create a Linked List 35->45 for second machine
    array[1] = None
    array[1] = push(array[1], 45)
    array[1] = push(array[1], 35)

    # Create Linked List 10->60->70->80 for third machine

    array[2] = None
    array[2] = push(array[2], 100)
    array[2] = push(array[2], 80)
    array[2] = push(array[2], 70)
    array[2] = push(array[2], 60)
    array[2] = push(array[2], 10)

    external_sort(array, N)
