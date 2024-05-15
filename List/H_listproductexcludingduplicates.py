'''
Python – List product excluding duplicates

This article focuses on one of the operations of getting the unique list from a list 
that contains a possible duplicated and finding its product. 
This operation has a large no. of applications and hence its knowledge is good to have.

The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
Duplication removal list product : 90
'''

import math

def product(list):
	s = set(list)
	return (math.prod(s))


l = [1, 3, 5, 6, 3, 5, 6, 1]
print(product(l))
