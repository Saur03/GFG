'''
Camel case of a given sentence
Given a sentence, task is to remove spaces from the sentence and rewrite in Camel case. 
It is a style of writing where we don’t have spaces and all words begin with capital letters.

Examples: 

Input  : I got intern at geeksforgeeks
Output : IGotInternAtGeeksforgeeks

Input :  Here comes the garden
Output : HereComesTheGarden
'''
# Python program to convert 
# given sentence to camel case.

# Function to remove spaces 
# and convert into camel case
def convert(s):
	if(len(s) == 0):
		return
	s1 = ''
	s1 += s[0].upper()
	for i in range(1, len(s)):
		if (s[i] == ' '):
			s1 += s[i + 1].upper()
			i += 1
		elif(s[i - 1] != ' '):
			s1 += s[i] 
	print(s1)	 
			

# Driver Code
def main():
	s = "I get intern at geeksforgeeks"
	convert(s)
	
if __name__=="__main__":
	main() 
	
