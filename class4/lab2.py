distance = float(input("How far is your destination (miles)? : "))
age = int(input("How old is the passenger?: "))

if distance < 1000:
    if age < 12:
        price = 200
    elif age >= 65:
        price = 250
    else:
        price = 300
else:
    if age < 12:
        price = 400
    elif age >= 65:
        price = 500
    else:
        price = 450

print("Your ticket will cost", price)
