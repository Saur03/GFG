'''
Python program to find the character position of Kth word from a list of strings.
Given a list of strings. The task is to find the index of the character position for the word, 
which lies at the Kth index in the list of strings.

Examples:

Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 21 
Output : 0
Explanation : 21st index occurs in “geeks” and point to “g” which is 0th element of word.

Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 15 
Output : 1
Explanation : 15th index occurs in “best” and point to “e” which is 1st element of word.
'''
# Python3 code to demonstrate working of
# Word Index for K position in Strings List
# Using nested loop

# initializing list
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 20

# initializing index counter
idx = 0

# iterating over each word in the list
for word in test_list:

	# if the kth position is in the current word
	if idx + len(word) > K:
		
		# printing result
		print("Index of character at Kth position word : " + str(K - idx))
		break
	
	# if the kth position is not in the current word
	else:
		idx += len(word)

# if the kth position is beyond the end of the list
else:
	print("K is beyond the end of the list")
