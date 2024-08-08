'''
Palindrome Substring Queries
Given a string and several queries on the substrings of the given input string to check 
whether the substring is a palindrome or not.

Examples : 

Suppose our input string is “abaaabaaaba” and the queries- [0, 10], [5, 8], [2, 5], [5, 9]
We have to tell that the substring having the starting and ending indices as above is a palindrome or not.
[0, 10] ? Substring is “abaaabaaaba” which is a palindrome. 
[5, 8] ? Substring is “baaa” which is not a palindrome. 
[2, 5] ? Substring is “aaab” which is not a palindrome. 
[5, 9] ? Substring is “baaab” which is a palindrome. 
'''
# A Python program to answer queries to check whether
# the substrings are palindrome or not
def isPalindrome(string: str, L: int, R: int) -> bool:
	# Keep comparing characters while they are same
	while R > L:
		if str[L] != str[R]:
			return False
		L += 1
		R -= 1
	return True

# Driver program to test above function
if __name__ == "__main__":
	str = "abaaabaaaba"
	n = len(str)
	queries = [[0, 10], [5, 8], [2, 5], [5, 9]]

	for q in queries:
		result = isPalindrome(str, q[0], q[1])
		if result:
			print("The substring [{},{}] is a palindrome".format(q[0], q[1]))
		else:
			print("The substring [{},{}] is not palindrome".format(q[0], q[1]))

