num = int(input("Enter the number you want to check"))

EvenOrOdd = "Even" if num%2 ==0 else "Odd"
PosOrNeg = "Positive" if num>=0 else "Negative"

print("Your number is", EvenOrOdd, "and is", PosOrNeg)

