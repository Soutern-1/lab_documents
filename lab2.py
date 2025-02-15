year = int(input("Enter the year you want to check: "))

leapYear = False

if year % 4 == 0:
    leapYear = True
    if year % 100 == 0:
        leapYear = False
        if year % 400 == 0:
            leapYear = True

else:
    leapYear = False

if leapYear == True: 
    print("Your year is a leap year")
elif leapYear == False:
    print("Your year is not a leap year")
else:
    print("error")