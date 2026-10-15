"""count the digits in a positive integer using a while loop"""

num=int(input("Enter a positive integer: "))

count=0
while num>0:
    num=num//10
    count+=1

print("the number of digits is: ", count)