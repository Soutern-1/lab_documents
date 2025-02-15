n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if n1>n2:
    result = n1 - n2
    print("The difference between the two numbers is: ", result)
elif n1<n2:
    result = n1+n2
    print('The sum of your numbers is: ', result)
elif n1==n2:
    result = n1 * n2
    print("The product of your numbers is: ",result)
else:
    print("error")