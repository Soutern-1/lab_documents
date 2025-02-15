n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

if n1>n2:
    value = n2
if n2>n1:
    value = n1

print("The lower number is ", value)
print("Bitsiwe and of number is", n1 & n2)
print("Bitwise or of number is", n1 | n2)
print("Bitwise not of first number is", ~n1)
print("1 bit left of 2nd number is ", n2<<1)
print("2 bit right of 2nd number is", n2>>2)

