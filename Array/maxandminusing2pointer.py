'''
Rearrange an array in maximum minimum form using Two Pointer Technique
Input: arr[] = {1, 2, 3, 4, 5, 6, 7} 
Output: arr[] = {7, 1, 6, 2, 5, 3, 4}

Input: arr[] = {1, 2, 3, 4, 5, 6} 
Output: arr[] = {6, 1, 5, 2, 4, 3} 
'''
def two_pointer(arr, n):
     # Auxiliary array to hold modified array
    temp = n*[None]
    min, max = 0, n-1
    
     # To indicate whether we need to copy remaining largest or smallest at next position
    flag = True
    
    for i in range(n):
        if flag is True:
            temp[i] = arr[max]
            max -= 1
        else:
              temp[i] = arr[min]  
              min += 1
         
        flag = bool(1-flag)
        
    # Copy temp[] to arr[]      
    for i in range(n):
         arr[i] = temp[i]
    return arr
     
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print("Original Array")
print(arr)
print("Modified Array")
print(two_pointer(arr, n))             
    