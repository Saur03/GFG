'''
Python – Reverse Row sort in Lists of List.
Sometimes, while working with data, we can have a problem in which we need to perform the sorting of rows of the matrix in descending order.
This kind of problem has its application in the web development and Data Science domain. 
Let’s discuss certain ways in which this task can be performed.

Output
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]
'''
# Python3 code to demonstrate
# Reverse Row sort in Lists of List
# using loop

# initializing list
test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

# printing original list
print("The original list is : " + str(test_list))

# Reverse Row sort in Lists of List
# using loop
for ele in test_list:
	ele.sort(reverse=True)

# printing result
print("The reverse sorted Matrix is : " + str(test_list))
