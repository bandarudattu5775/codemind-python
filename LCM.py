v,k=map(int,input().split())
I=0
if v>k:
    I=v
    while(I):
        if(I%v==0 and I%k==0):
            print(I)
            break
        I+=1
else:
    I=k
    while(I):
        if(I%v==0 and I%k==0):
            print(I)
            break
        I+=1