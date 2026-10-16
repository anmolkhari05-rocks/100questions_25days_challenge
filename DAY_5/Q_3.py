"""Check whether a number is a palindrome using arithmetic  operations"""

n = int(input("Enter a number: "))

if n < 0:
    print("Not a palindrome")
else:
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    if original == reverse:
        print("Palindrome number")
    else:
        print("Not a palindrome")