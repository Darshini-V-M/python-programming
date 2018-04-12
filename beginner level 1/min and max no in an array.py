y=raw_input()
n=int(y)
a=[]
for i in range(n):
	u=raw_input()
	b=int(u)
	a.append(b)
min=int(a[0])
max=a[0]
for i in range(n):
	if(a[i]<min):
		min=a[i]
	else:
		c=0
for i in range(n):
	if(a[i]>max):
		max=a[i]
	else:
		c=0
print min,max
