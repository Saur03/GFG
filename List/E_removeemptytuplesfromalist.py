'''
In this article, we will see how can we remove an empty tuple from a given list of tuples. We will find various ways, in which we can perform this task of removing tuples using various methods and ways in Python. 

Examples:

Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]

Input : tuples = [(”,”,’8′), (), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”), (),  (”,”),()]
Output : [(”, ”, ‘8’), (‘0′, ’00’, ‘000’), (‘birbal’, ”, ’45’), (”, ”)]
'''
# Python2 program to remove empty tuples
# from a list of tuples function to remove 
# empty tuples using filter
def Remove(tuples):
	tuples = filter(None, tuples)
	return tuples

# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
		('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))
