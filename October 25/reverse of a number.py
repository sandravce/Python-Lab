'''Create a function to read a number (minimum 4 digits) from the user and find the reverse of the number
using loop in another function and display both number and reverse of the number.
'''

def reverse_number(num):
    rev = 0
    while num:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

num = int(input("Enter a number with at least 4 digits: "))
while len(str(num)) < 4:
    num = int(input("Please enter at least 4 digits: "))

print("Original Number:", num)
print("Reversed Number:", reverse_number(num))
