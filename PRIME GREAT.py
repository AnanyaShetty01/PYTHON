count=0
for i in range(1000,100,-1):
    c=0
    for j in range(2,i):
        if(i%j==0):
            c=c+1
    if(c==0):
        count=count+1
        if(count<20):
            print(i,end= " ")