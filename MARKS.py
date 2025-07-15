sum=0
while (True):
    x=int(input("Enter the marks: "))
    if x<=100:
        sum+=x
    if x==0:
        break
print(sum)