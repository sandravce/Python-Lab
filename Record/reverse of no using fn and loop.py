'''Write a Python program to get a string from an input string where all occurrences of first character
replaced with ‘$’, except first character. [eg: onion -> oni$n'''

print("REVERSE OF THE NUMBER USING FUNCTION AND LOOP")
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


