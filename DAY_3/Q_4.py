""" check wheather a year is a leap year or not"""

year=int(input("Enter the year to be checked: "))

if year%4==0:
    print("congratulations you have one day more")
elif year%400==0:
    print("congratulations you have one day more")
elif year%100==0:
    print("sorry your feb month is of 28 only")
else:
    print("sorry your feb month is of 28 only")