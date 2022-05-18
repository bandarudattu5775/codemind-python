r=int(input())
I=0
v=list(map(int,input().split()))
for k in range(0,len(v)):
    if v[k]%2!=0:
        I+=1
if I<=2:
    print('YES')
else:
    print('NO')