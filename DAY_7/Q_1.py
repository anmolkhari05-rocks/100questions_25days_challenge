"""write a function that returns a square of a number"""


def cal_square(num):
    return num*num

num = int(input("enter a number: "))
result = cal_square(num)

print("the square of the number is:", result)