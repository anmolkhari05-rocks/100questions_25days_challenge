"""print the multiplication table of the number upto 10"""

num=int(input("Enter the number whose table is to be printed: "))
i=1
while i<=10:
    print(num, "x", i,"=", num*i)
    i+=1