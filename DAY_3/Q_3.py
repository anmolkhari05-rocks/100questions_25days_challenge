"""find the largest number among three without using max() function"""


"""problem in case 3,2,3"""


num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if num1>num2 and num2>num3:                         
    print("num1 is the largest number among three")
if num1>num2 and num3>num2:
    print("num1 is the largest number among three")
elif num2>num1 and num1>num3:
    print("num2 is the largest number among the three ")
elif num3>num1 and num1>num2:
    print("num3 is the largest number among the three ")
elif num3>num2 and num2>num1:
    print("num3 is the largest number among the three ")
elif num1==num2 and num1>num3:
    print("num1 and num2 are equal and greater than num3")
elif num1==num2 and num1<num3:
    print("num1 and num2 are equal and less than num3")
elif num2==num3 and num2>num1:
    print("num2 and num3 are equal and greater than num1")
elif num2==num3 and num2<num1:
    print("num2 and num3 are equal and less than num1")
elif num1==num3 and num1>num2:
    print("num1 and num3 are equal and greater than num2")
elif num1==num3 and num1<num2:
    print("num1 and num3 are equal and less than num2")
else:
    print("all the three numbers are equal")