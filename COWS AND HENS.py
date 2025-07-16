legs=int(input("Enter the total number of legs: "))
heads=int(input("Enter the total number of heads: "))
flag=False
for hen in range(heads):
    cow=heads-hen
    if(cow*4 + hen*2 == legs):
        print("COWS: ")
        print("HENS: ")
        flag=True
        break
if(not flag):
    print("No solution")
    