'''
Find the first non-repeating character from a stream of characters
'''
def FirstNonRepeating(A):
		# Code here
		list = [] 
		mp = {}
		ans = ''

		for ch in A:
			if ch not in mp: # new character visited first time
				list.append(ch)
				mp[ch] = 1
			else:
				# any repeated character encountered
				if ch in list:
					list.remove(ch)
			ans += list[0] if list else '#'

		return ans
l = "geeksforgeeksandgeeksquizfor"
ans1 = FirstNonRepeating(l)
print(ans1)
