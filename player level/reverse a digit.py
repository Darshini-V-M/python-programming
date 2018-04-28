Num = int(input())
Reverse = 0
while(Num > 0):
     Remind = Num%10
     Reverse = (Reverse *10) + Remind
     Num = Num//10
print("%d" %Reverse)
