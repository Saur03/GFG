'''
Find all even length binary sequences with same sum of first and second half bits
Given a number n, find all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.

Examples: 
Input:  N = 2
Output: 
0101 1111 1001 0110 0000 1010 

Input:  N = 3
Output:  
011011 001001 011101 010001 101011 111111
110011 101101 100001 110101 001010 011110 
010010 001100 000000 010100 101110 100010 
110110 100100 
'''
# Python3 program to print even length binary sequences
# whose sum of first and second half bits is same

# Function to print even length binary sequences
# whose sum of first and second half bits is same

# diff --> difference between sums of first n bits
# and last n bits
# out --> output array
# start --> starting index
# end --> ending index
def findAllSequences(diff, out, start, end):

	# We can't cover difference of more than n with 2n bits
	if (abs(diff) > (end - start + 1) // 2):
		return;

	# if all bits are filled
	if (start > end):
		# if sum of first n bits and last n bits are same
		if (diff == 0):
			print(''.join(list(out)),end=" ");
		return;

	# fill first bit as 0 and last bit as 1
	out[start] = '0';
	out[end] = '1';
	findAllSequences(diff + 1, out, start + 1, end - 1);

	# fill first and last bits as 1
	out[start] = out[end] = '1';
	findAllSequences(diff, out, start + 1, end - 1);

	# fill first and last bits as 0
	out[start] = out[end] = '0';
	findAllSequences(diff, out, start + 1, end - 1);

	# fill first bit as 1 and last bit as 0
	out[start] = '1';
	out[end] = '0';
	findAllSequences(diff - 1, out, start + 1, end - 1);

# Driver program

# input number
n = 2;

# allocate string containing 2*n characters
out=[""]*(2*n);

findAllSequences(0, out, 0, 2*n - 1);

# This code is contributed by mits
