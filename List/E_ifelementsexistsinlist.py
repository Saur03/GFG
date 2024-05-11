'''
Check if element exists in list in Python
Last Updated : 26 Mar, 2024
The list is an important container in Python as it stores elements of all the data types as a collection. Knowledge of certain list operations is necessary for day-day programming. This article discusses the Fastest way to check if a value exists in a list or not using Python.

Example

Input: test_list = [1, 6, 3, 5, 3, 4]
            3  # Check if 3 exist or not.
Output: True
Explanation: The output is True because the element we are looking is exist in the list.
'''
lst=[ 1, 6, 3, 5, 3, 4 ] 
#checking if element 7 is present
# in the given list or not
i=7 
# if element present then return
# exist otherwise not exist
if i in lst: 
    print("exist") 
else: 
    print("not exist")
