'''
Count of total anagram substrings.
Given a string of lower alphabet characters, count total substring of this string which are anagram to each other.

Examples:

Input  : str = “xyyx”
Output : 4
Total substrings of this string which
are anagram to each other are 4 which 
can be enumerated as,
{“x”, “x”}, {"y", "y"}, {“xy”, “yx”}, 
{“xyy”, “yyx”}

Input  : str = "geeg"
Output : 4
'''
# Python3 program to count total anagram
# substring of a string
def countOfAnagramSubstring(s):
	
	# Returns total number of anagram substrings in s
	n = len(s)
	mp = dict()
	
	# loop for length of substring
	for i in range(n):
		sb = ''
		for j in range(i, n):
			sb = ''.join(sorted(sb + s[j]))
			mp[sb] = mp.get(sb, 0)
			
			# increase count corresponding
			# to this dict array
			mp[sb] += 1

	anas = 0
	
	# loop over all different dictionary 
	# items and aggregate substring count
	for k, v in mp.items():
		anas += (v*(v-1))//2
	return anas

# Driver Code
s = "xyyx"
print(countOfAnagramSubstring(s))

