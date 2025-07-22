Indian=["Samosa","Butter chicken","Mutton Biryani"]
Chinese=["Fried rice","Paneer chilli","Mushroom manchurian"]
Italian=["Pizza","Pasta","Speghatti"]

dish=input("Enter the dish name:")

if dish in Indian:
    print("This is Indian")
elif dish in Chinese:
    print("This is Chinese")
elif dish in Italian:
    print("This is Italian")
else:
    print("Sorry I don't know which dish is",dish)