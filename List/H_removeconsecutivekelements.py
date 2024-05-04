'''
Python- Remove Consecutive K element records
Last Updated : 08 May, 2023
Sometimes, while working with Python records, we can have a problem in which we need to remove records on the basis of presence of consecutive K elements in tuple. This kind of problem is peculiar but can have applications in data domains. Let’s discuss certain ways in which this task can be performed.

Input : test_list = [(4, 5), (5, 6), (1, 3), (0, 0)] K = 0 
Output : [(4, 5), (5, 6), (1, 3)] 

Input : test_list = [(4, 5), (5, 6), (1, 3), (5, 4)] K = 5 
Output : [(4, 5), (5, 6), (1, 3), (5, 4)]
'''

test_list = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]
K = 6
 
temp_list = []
for item in test_list:
    skip = False
    for i in range(len(item)-1):
        if item[i] == K and item[i+1] == K:
            skip = True
            break
    if not skip:
        temp_list.append(item)
res = temp_list
 
print("The records after removal : ", res)