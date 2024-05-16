'''
In this problem we need to find out the next greater element of each element so we can use monotonic stack in this question. 
Why? Because we can store the elements in the stack in increasing order of index and value 
and if current value of stack does not satisfy the current condition of having greater than current array element 
then this stack value never contribute in our answer so we can pop this value which maintains the monotonic behaviour of the stack.
'''
def printNGE(arr, n):
    stack = []

    # push the first element to stack
    stack.append(arr[0])

    # iterate for rest of the elements
    for i in range(1, n):

        if not stack:
            stack.append(arr[i])
            continue

        # if stack is not empty, then pop an element from stack.
        # If the popped element is smaller than next, then
        # a) print the pair
        # b) keep popping while elements are smaller and stack is not empty
        while stack and stack[-1] < arr[i]:
            print(stack.pop(), "-->", arr[i])

        # push next to stack so that we can find next greater for it
        stack.append(arr[i])

    # After iterating over the loop, the remaining elements in stack do not have the next greater element, so print -1 for them
    while stack:
        print(stack.pop(), "-->", -1)

# Driver code
arr = [11, 13, 21, 3]
n = len(arr)
printNGE(arr, n)
