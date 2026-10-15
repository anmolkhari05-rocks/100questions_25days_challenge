"""find the sum of the first n natural number using loop"""

n=int(input("Enter the last digit till the sum is to be calculate: "))
sum=0
for i in range(1, n+1):
    sum=sum+i
    print("the sum of natiral numbers is: ", sum)