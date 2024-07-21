'''
Second most repeated word in a sequence
Given a sequence of strings, the task is to find out the second most repeated (or frequent) string 
in the given sequence.(Considering no two words are the second most repeated, there will be always a single word).

Examples: 

Input : {"aaa", "bbb", "ccc", "bbb", 
         "aaa", "aaa"}
Output : bbb
Input : {"geeks", "for", "geeks", "for", 
          "geeks", "aaa"}
Output : for
'''
# Python3 program to find out the second most repeated word 

# Function to find the word 
def secMostRepeated(seq): 
	
	# Store all the words with its occurrence 
	occ = {} 
	for i in range(len(seq)): 
		occ[seq[i]] = occ.get(seq[i], 0) + 1

	# Find the second largest occurrence 
	first_max = -10**8
	sec_max = -10**8

	for it in occ: 
		if (occ[it] > first_max): 
			sec_max = first_max 
			first_max = occ[it] 
			
		elif (occ[it] > sec_max and
			occ[it] != first_max): 
			sec_max = occ[it] 

	# Return with occurrence equals 
	# to sec_max 
	for it in occ: 
		if (occ[it] == sec_max): 
			return it 

# Driver code 
if __name__ == '__main__': 
	
	seq = [ "ccc", "aaa", "ccc", 
			"ddd", "aaa", "aaa" ] 
	print(secMostRepeated(seq)) 

