'''
Count words in a given string
'''
OUT = 0
IN = 1
def countWords(string):
    state = OUT
    wc = 0
    for i in range(len(string)):
        # If next character is a separator, set the state as OUT
        if (string[i] == ' ' or string[i] == '\n' or string[i] == '\t'):
             state = OUT
             # If next character is not a word  separator and state is OUT, then set the state as IN and increment word count
        elif state == OUT:
             state = IN
             wc += 1     
             
    return wc

string = "One two  three \n four \tfive "
print("No. of words : " + str(countWords(string)))

         