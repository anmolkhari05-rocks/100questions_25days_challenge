"""swap two variables using a temporary variable,then without one """

a=int(input("Enter the first value: "))
b=int(input("Enter the second value: "))

temp=a
a=b
b=temp

print("values after the swaping:")
print("first value will be: ", a)
print("second value will be: ", b)