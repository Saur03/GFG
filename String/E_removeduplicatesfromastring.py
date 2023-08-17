'''
Remove duplicates from a given string
'''
def remove_dup(string):
    lst = []
    
    for char in string:
        if char not in lst:
            lst.append(char)
    st = "".join(lst)
    return st

s="geeksforgeeks"
print(remove_dup(s))        
            