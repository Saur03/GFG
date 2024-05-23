'''
Finite Recursion occurs when the recursion terminates after a finite number of recursive calls. 
A recursion terminates only when a base condition is met.
'''
# Python program to demsonstrate Finite Recursion
# Recursive function
def Geek( N):

	# Base condition
	# When this condition is met,
	# the recursion terminates
	if (N == 0):
		return

	# Pr the current value of N
	print( N, end =" " )

	# Call itself recursively
	Geek(N - 1)


# Driver code
# Initial value of N
N = 5

# Call the recursive function
Geek(N)

'''
Infinite Recursion occurs when the recursion does not terminate after a finite number of recursive calls. 
As the base condition is never met, the recursion carries on infinitely.
'''
# Python3 to demsonstrate Infinite Recursion

# Recursive function
def Geek(N):
	
	# Base condition
	# This condition is never met here
	if (N == 0):
		return

	# Print the current value of N
	print(N, end = " " )

	# Call itself recursively
	Geek(N)

# Driver code

# Initial value of N
N = 5

# Call the recursive function
Geek(N)
