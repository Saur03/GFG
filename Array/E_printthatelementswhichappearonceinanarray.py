'''
Find the element that appears once in an array where every other element appears twice
Example : 

Input:  arr[] = {2, 3, 5, 4, 5, 3, 4}
Output: 2 
'''
def findSingleelement(A, ar_size):
    for i in range(ar_size):
        count = 0
        for j in range(ar_size):
            # Count the frequency of the element
            if(A[i] == A[j]):
                count += 1
        # If the frequency of the element is one        
        if(count == 1):
            return A[i]        
    
    # If no element exist at most once  
    return -1    

ar = [2, 3, 5, 4, 5, 3, 4]
n = len(ar)
print("Element occurring once is", findSingleelement(ar, n))