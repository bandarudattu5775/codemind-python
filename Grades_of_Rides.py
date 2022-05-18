v,k,I=map(int,input().split())
if(v>50 and k>60 and I>100):
    print("10")
elif(v>50 and k>60):
    print("9")
elif(k>60 and I>100):
    print("8")
elif(v>50 and I>100):
    print("7")
elif(v>50 or k>60 or I>100):
    print("6")
else:
    print("5")

    
    