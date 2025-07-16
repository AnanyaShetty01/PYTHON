import time
str1=input("Enter Sentence ")
c=0
for i in range(len(str1)):
    if(str1[i]==" " and str1[i+1]!=" "):
        c=c+1
time.sleep(2)
print("The words are", c+1)