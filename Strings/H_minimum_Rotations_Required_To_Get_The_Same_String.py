'''
Minimum rotations required to get the same string.
Given a string, we need to find the minimum number of rotations required to get the same string.

Examples: 

Input : s = "geeks"
Output : 5

Input : s = "aaaa"
Output : 1
'''
# Python program to determine minimum number 
# of rotations required to yield same 
# string. 

# Returns count of rotations to get the 
# same string back. 
def findRotations(Str): 

	ans = 0 # to store the answer
	n = len(Str) # length of the String
	
	# All the length where we can partition
	for i in range(1 , len(Str) - 1):

		# right part + left part = rotated String
		# we are checking whether the rotated String is equal to 
		# original String
		if(Str[i: n] + Str[0: i] == Str):
			ans = i
			break

	if(ans == 0):
		return n
	return ans

# Driver code 
Str = "abc"
print(findRotations(Str))

