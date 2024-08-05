'''
Form minimum number from given sequence.
Auxiliary Given a pattern containing only I’s and D’s. 
I for increasing and D for decreasing. Device an algorithm to print the minimum number following that pattern. 
Digits from 1-9 and digits can’t repeat.

Examples: 

   Input: D        Output: 21
   Input: I        Output: 12
   Input: DD       Output: 321
   Input: II       Output: 123
   Input: DIDI     Output: 21435
   Input: IIDDD    Output: 126543
   Input: DDIDDIID Output: 321654798
'''
# Python3 program to print minimum number that 
# can be formed from a given sequence of Is and Ds 

# Prints the minimum number that can be formed from 
# input sequence of I's and D's 
def PrintMinNumberForPattern(arr): 

	# Initialize current_max (to make sure that 
	# we don't use repeated character 
	curr_max = 0

	# Initialize last_entry (Keeps track for 
	# last printed digit) 
	last_entry = 0
	i = 0

	# Iterate over input array 
	while i < len(arr): 

		# Initialize 'noOfNextD' to get count of 
		# next D's available 
		noOfNextD = 0
		if arr[i] == "I": 

			# If letter is 'I' 

			# Calculate number of next consecutive D's 
			# available 
			j = i + 1
			while j < len(arr) and arr[j] == "D": 
				noOfNextD += 1
				j += 1
			if i == 0: 
				curr_max = noOfNextD + 2
				last_entry += 1

				# If 'I' is first letter, print incremented 
				# sequence from 1 
				print("", last_entry, end = "") 
				print("", curr_max, end = "") 

				# Set max digit reached 
				last_entry = curr_max 
			else: 

				# If not first letter 

				# Get next digit to print 
				curr_max += noOfNextD + 1

				# Print digit for I 
				last_entry = curr_max 
				print("", last_entry, end = "") 

			# For all next consecutive 'D' print 
			# decremented sequence 
			for k in range(noOfNextD): 
				last_entry -= 1
				print("", last_entry, end = "") 
				i += 1

		# If letter is 'D' 
		elif arr[i] == "D": 
			if i == 0: 

				# If 'D' is first letter in sequence 
				# Find number of Next D's available 
				j = i + 1
				while j < len(arr) and arr[j] == "D": 
					noOfNextD += 1
					j += 1

				# Calculate first digit to print based on 
				# number of consecutive D's 
				curr_max = noOfNextD + 2

				# Print twice for the first time 
				print("", curr_max, curr_max - 1, end = "") 

				# Store last entry 
				last_entry = curr_max - 1
			else: 

				# If current 'D' is not first letter 

				# Decrement last_entry 
				print("", last_entry - 1, end = "") 
				last_entry -= 1
		i += 1
	print() 

# Driver code 
if __name__ == "__main__": 
	PrintMinNumberForPattern("IDID") 
	PrintMinNumberForPattern("I") 
	PrintMinNumberForPattern("DD") 
	PrintMinNumberForPattern("II") 
	PrintMinNumberForPattern("DIDI") 
	PrintMinNumberForPattern("IIDDD") 
	PrintMinNumberForPattern("DDIDDIID") 

