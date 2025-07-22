n = int(input("Enter a number: "))
seen = []

while n not in seen:
    seen.append(n)
    n = sum(int(i)**2 for i in str(n))

if n == 1:
    print("ROUND NUMBER")
else:
    print("Not")
