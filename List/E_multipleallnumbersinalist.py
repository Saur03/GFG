'''
Python | Multiply all numbers in the list. Given a list, print the value obtained after multiplying all numbers in a Python list. 
Examples: 
Input :  list1 = [1, 2, 3]
Output : 6
Explanation: 1*2*3=6

Input : list1 = [3, 2, 4]
Output : 24 
'''
'''
Lambda’s definition does not include a “return” statement, it always contains an expression that is returned. 
We can also put a lambda definition anywhere a function is expected, and we don’t have to assign it to a variable at all. 
This is the simplicity of lambda functions. The reduce() function in Python takes in a function and a list as an argument. 
The function is called with a lambda function and a list and a new reduced result is returned. 
This performs a repetitive operation over the pairs of the list.

Example :  In this example the below code uses Python’s `functools.reduce` with a lambda function to multiply all values in lists `[1, 2, 3]` and `[3, 2, 4]`. 
The results, 6 and 24, are printed.
'''
# Python3 program to multiply all values in the
# list using lambda function and reduce()
from functools import reduce
list1 = [1, 2, 3]
list2 = [3, 2, 4]

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)
