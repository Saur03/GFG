'''
Sort an array which contain 1 to n values
Input : arr[] = {10, 7, 9, 2, 8, 3, 5, 4, 6, 1};
Output : 1 2 3 4 5 6 7 8 9 10 
'''
def sort(arr, n):
    temp = 0
    print("Elements of original array: ");
    for i in range(0, len(arr)):
          print(arr[i], end=" ");
          
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
             if (arr[i] > arr[j]):
                 temp = arr[i];
                 arr[i] = arr[j];
                 arr[j] = temp;
    print();
    
arr = [3, 2, 5, 6, 1, 4]
n = len(arr)
sort(arr, n)
for i in range(0, n):
    print(arr[i], end=" ")
    
  