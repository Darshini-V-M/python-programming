a=raw_input()
b=raw_input()
c=raw_input()
if isinstance(a,str) and isinstance(b,str) and isinstance(c,str):
	if(((a>='a') and (a<='z')) and ((b>='a') and (b<='z')) and ((c>='a') and (c<='z'))):
		print("invalid")
	else:
		a=int(a)
		b=int(b)
		c=int(c)
		if (a>=b and a>=c):
			print a
		elif (b>=a and b>=c):
			print b
		else: 
			print c
else:
	print("enter a valid number")
	
	
	
# your code goes here
