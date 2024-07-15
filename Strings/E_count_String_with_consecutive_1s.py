'''
Count strings with consecutive 1’s

Given a number n, count number of n length strings with consecutive 1’s in them.

Examples: 

Input  : n = 2
Output : 1
There are 4 strings of length 2, the
strings are 00, 01, 10 and 11. Only the 
string 11 has consecutive 1's.

Input  : n = 3
Output : 3
There are 8 strings of length 3, the
strings are 000, 001, 010, 011, 100, 
101, 110 and 111.  The strings with
consecutive 1's are 011, 110 and 111.

Input : n = 5
Output : 19
'''
# Python program to count all distinct
# binary strings with two consecutive 1's

# Gives count of n length binary
# strings with consecutive 1's
def countStrings(n, ind, s, ans):
	if ind == n:
		count = 0
		temp = 0
		for i in range(n):
			if s[i] == '1':
				temp += 1
			else:
				temp = 0
			count = max(count, temp)
		if count >= 2:
			ans[0] += 1
		return
	
	countStrings(n, ind + 1, s + "0", ans)
	countStrings(n, ind + 1, s + "1", ans)

# Driver code
if __name__ == '__main__':
	ans = [0]
	countStrings(3, 0, "", ans)
	print(ans[0])

