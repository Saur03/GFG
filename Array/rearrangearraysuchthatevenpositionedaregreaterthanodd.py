'''
Rearrange array such that even positioned are greater than odd
Input : A[] = {1, 2, 2, 1}
Output :  1 2 1 2
Explanation : 
For 1st element, 1  1, i = 2 is even.
3rd element, 1  1, i = 4 is even.
Input : A[] = {1, 3, 2}
Output : 1 3 2
Explanation : 
Here, the array is also sorted as per the conditions. 
1  1 and 2 < 3.
'''
def assign(a, n):
    #sort the array
    a.sort()
    ans = [0] * n
    p = 0
    q = n - 1
    for i in range(n):
        # Assign even indexes with maximum elements
        if (i + 1) % 2 == 0:
            ans[i] = a[q]
            q = q - 1
        # Assign odd indexes with remaining elements    
        else:
            ans[i] = a[p]
            p = p + 1 
    # Print result           
    for i in range(n):
        print(ans[i], end = " ")
        
A = [ 1, 3, 2, 2, 5 ]
n = len(A)
assign(A, n)        
        
        