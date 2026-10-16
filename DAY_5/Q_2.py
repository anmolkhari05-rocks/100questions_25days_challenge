"""Reverse the digits of an integer without converting it to a string"""

n = int(input("Enter an integer: "))
num = abs(n)
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if n < 0:
    reverse = -reverse

print("Reversed number:", reverse)