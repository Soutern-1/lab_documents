condition = int(input("Enter your condition based on the number. Critical condition = 1, Serious condition = 2, Stable condition = 3: "))
age = int(input("Enter your age: "))


if condition == 1:
    if age<12 or age>=65:
        priority = "Highest Priority"
    else: 
        priority = "Emergency"
elif condition == 2:
    if age>12 and age<65:
        priority = "Medium priority"
    else:
        priority = "Emergency"
elif condition == 3:
    if age>=18 or age<65:
        priority = "Lowest priority"
    else:
        priority = "Emergency"

print(priority)
