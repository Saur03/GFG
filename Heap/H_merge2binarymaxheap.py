'''
Merge two binary Max Heaps

Given two binary max heaps as arrays, the task is to merge the given heaps.
Examples : 

Input: a = {10, 5, 6, 2}, b = {12, 7, 9}
Output: {12, 10, 9, 2, 5, 7, 6}

Input: a = {2, 5, 1, 9, 12}, b = {3, 7, 4, 10}
Output: {12, 10, 7, 9, 5, 3, 1, 4, 2}
'''
def mergeHeaps(a, b, n, m):
    # vis_next1 & vis_next2 tells us if the next element of array "a" 
    # and array "b" is visited or not, respectively.
    vis_next1 = False
    vis_next2 = False
    # i & j are the current indices of arrays "a" and "b", respectively.
    i = 0
    j = 0

    # Loop until the end of array "a" or "b"
    while i != n and j != m:
        max1 = i
        max2 = j

        # Check if the next element of array "a" is greater than 
        # the current element
        if i + 1 != n and not vis_next1 and a[i + 1] > a[i]:
            max1 = i + 1

        # Check if the next element of array "b" is greater than 
        # the current element
        if j + 1 != m and not vis_next2 and b[j + 1] > b[j]:
            max2 = j + 1

        # Compare the maximum elements from both arrays
        if a[max1] > b[max2]:
            print(a[max1], end=" ")

            # Update index and vis_next1 for array "a"
            if max1 == i + 1:
                vis_next1 = True
            else:
                if vis_next1:
                    i += 2
                    vis_next1 = False
                else:
                    i += 1
        else:
            print(b[max2], end=" ")

            # Update index and vis_next2 for array "b"
            if max2 == j + 1:
                vis_next2 = True
            else:
                if vis_next2:
                    j += 2
                    vis_next2 = False
                else:
                    j += 1

    # Print remaining elements of array "b" if array "a" is exhausted
    if i == n:
        while j != m:
            print(b[j], end=" ")
            j += 1
            if vis_next2:
                vis_next2 = False
                j += 1
    # Print remaining elements of array "a" if array "b" is exhausted
    else:
        while i != n:
            print(a[i], end=" ")
            i += 1
            if vis_next1:
                vis_next1 = False
                i += 1

# Driver's code
if __name__ == "__main__":
    a = [10, 5, 6, 2]
    b = [12, 7, 9]
    N = len(a)
    M = len(b)

    # Function call
    mergeHeaps(a, b, N, M)
    
