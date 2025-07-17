n = int(input("Enter the number of teams: "))
teams = [input(f"Enter team name {i+1}: ") for i in range(n)]
meet = int(input("Enter number of meetings: "))

match = []
for i in range(n - 1):
    for j in range(i + 1, n):
        for k in range(meet):
            match.append([teams[i], teams[j]])

for i, m in enumerate(match):
    print(f"{i+1}. {m[0]} vs {m[1]}")
