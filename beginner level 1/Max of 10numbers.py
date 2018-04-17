a=[]
for i in range(10):
	u=raw_input()
	b=int(u)
	a.append(b) 
max=a[0]
for i in range(10):
	if(a[i]>max):
		max=a[i]
	else:
		c=0
print max
