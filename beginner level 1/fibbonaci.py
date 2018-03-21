n=raw_input()
n=int(n)
count=0
n1=0
n2=1
print n1,
print n2,
while(n>count):
	n3=n1+n2
	n1=n2
	n2=n3
	count=count+1
	print n3,
