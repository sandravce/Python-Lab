'''Create a function to read a number (minimum 4 digits) from the user and find the reverse of the number
using loop in another function and display both number and reverse of the number.'''

def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

def main():
    while True:
        user_input = input("Enter a number with at least 4 digits: ")
        if user_input.isdigit() and len(user_input) >= 4:
            number = int(user_input)
            break
        else:
            print("Invalid input. Please enter a number with at least 4 digits.")

    reversed_num = reverse_number(number)

    print(f"Original Number: {number}")
    print(f"Reversed Number: {reversed_num}")

# Run the main function
main()










