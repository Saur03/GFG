'''
Find Subarray with given sum | Set 1 (Non-negative Numbers)
Examples: 

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4
Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33
'''
def subArraySum(arr, n, sum):
     for i in range(0,n):
         currentSum = arr[i]
         if(currentSum == sum):
             print("Sum found at indexes",i)
             return
         else:
            for j in range(i+1,n):
                 currentSum += arr[j]
                 if(currentSum == sum):
                     print("Sum found between indexes",i,"and",j)
                     return
     print("No Subarray Found") 
     
if __name__ == "__main__":
    arr = [15,2,4,8,9,5,10,23]
    n = len(arr)
    sum = 23
    subArraySum(arr, n, sum)     