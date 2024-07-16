'''
Add n binary strings.
Given n binary strings, return their sum (also a binary string).

Examples:  

Input:  arr[] = ["11", "1"]
Output: "100"
Input : arr[] = ["1", "10", "11"]
Output : "110" 
'''
# Python3 program to add n binary strings

# This function adds two binary strings and 
# return result as a third string
def addBinaryUtil(a, b):
	
	result = ""; # Initialize result
	s = 0;	 # Initialize digit sum

	# Traverse both strings 
	# starting from last characters
	i = len(a) - 1;
	j = len(b) - 1;
	while (i >= 0 or j >= 0 or s == 1):

		# Compute sum of last digits and carry
		s += (ord(a[i]) - ord('0')) if(i >= 0) else 0;
		s += (ord(b[j]) - ord('0')) if(j >= 0) else 0;

		# If current digit sum is 1 or 3, 
		# add 1 to result
		result = chr(s % 2 + ord('0')) + result;

		# Compute carry
		s //= 2;

		# Move to next digits
		i -= 1;
		j -= 1;

	return result;

# function to add n binary strings
def addBinary(arr, n):
	result = "";
	for i in range(n):
		result = addBinaryUtil(result, arr[i]);
	return result;

# Driver code
arr = ["1", "10", "11"];
n = len(arr);
print(addBinary(arr, n));
	
