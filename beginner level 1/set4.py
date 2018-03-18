string=raw_input("Enter string:")
char=0
word=1
for i in string:
    char=char+1
print("Number of characters in the string:")
c=len(string.replace(" ", ""))
print (c)
