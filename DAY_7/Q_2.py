"""write a function that accepts two number and returns the larger one"""

def find_larger_number(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

result=find_larger_number(num1,num2)
print("the larger number is:",result)