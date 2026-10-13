"""input a number and print its type after converting it into int , float and string"""

a = input("enter a number: ")

integer_num = int(float(a))
float_num= float(a)
string_num = str(a)

print("integer:",integer_num)
print("type:",type(integer_num))

print("float:", float_num)
print("type:", type(float_num))

print("string:" , string_num)
print("type:" , type(string_num))