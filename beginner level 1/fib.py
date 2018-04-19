p=raw_input()
p=int(p)
count=0
n1=0
n=1
print n,
while(p-1>count):
	n3=n1+n
	n1=n
	n=n3
	count=count+1
	print n,
