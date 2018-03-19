a=raw_input()
b=raw_input()
c=raw_input()
if a.isdigit() and b.isdigit() and c.isdigit():
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
