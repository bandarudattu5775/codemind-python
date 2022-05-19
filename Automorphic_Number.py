n=int(input())
t=n
I=0
while(n>0):
    I+=1
    n=n//10
n=t*t
n=n%(pow(10,I))
if(t==n):
   print('Automorphic Number')
else:
   print('Not an Automorphic Number')