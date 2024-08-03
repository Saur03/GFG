'''
Print shortest path to print a string on screen

Given a screen containing alphabets from A-Z, we can go from one character to another characters using a remote. 
The remote contains left, right, top and bottom keys.
Find shortest possible path to type all characters of given string using the remote. 
Initial position is top left and all characters of input string should be printed in order.

Screen: 
A B C D E
F G H I J
K L M N O
P Q R S T
U V W X Y
Z

Example: 
 

Input: “GEEK”
Output: 
Move Down
Move Right
Press OK
Move Up
Move Right
Move Right
Move Right
Press OK
Press OK
Move Left
Move Left
Move Left
Move Left
Move Down
Move Down
Press OK

If row difference is negative, we move up
If row difference is positive, we move down
If column difference is negative, we go left
If column difference is positive, we go right
'''
# Python 3 program to print shortest possible path to type all characters of given string using a remote

# Function to print shortest possible path to type all characters of given string using a remote
def printPath(str):
	i = 0
	
	# start from character 'A' present 
	# at position (0, 0)
	curX = 0
	curY = 0
	while (i < len(str)):
		
		# find coordinates of next character
		nextX = int((ord(str[i]) - ord('A')) / 5)
		nextY = (ord(str[i]) - ord('B') + 1) % 5

		# Move Up if destination is above
		while (curX > nextX):
			print("Move Up")
			curX -= 1

		# Move Left if destination is to the left
		while (curY > nextY):
			print("Move Left")
			curY -= 1

		# Move down if destination is below
		while (curX < nextX):
			print("Move Down")
			curX += 1

		# Move Right if destination is to the right
		while (curY < nextY):
			print("Move Right")
			curY += 1

		# At this point, destination is reached
		print("Press OK")
		i += 1

# Driver code
if __name__ == '__main__':
	str = "COZY"

	printPath(str)

