q=[]
for i in range(10):
	u=raw_input()
	b=int(u)
	q.append(b) 
max=a[0]
for i in range(10):
	if(q[i]>max):
		max=q[i]
	else:
		c=0
print max
