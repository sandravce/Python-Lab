print("\n")
print("MENU PROGRAM\n")
print("1:occurence of a word:\n")
print("2:frequency of a character:\n")
print("3:factors of a given number:\n")
print("4:exit:\n")

while True:
    choice = int(input("enter your choice:\n"))

    if choice > 4:
        print("invalid option")

    elif choice == 1:
        print("occurence of a word")
        text = input("enter the text:")
        words = text.split()
        count = {}
        for w in words:
            count[w] = count.get(w, 0) + 1
        print(count)

    elif choice == 2:
        print("frequency of a character")
        s = input("enter the string:\n")
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        print(count)

    elif choice == 3:
        print("factors of a given number")
        num = int(input("enter the number u want to find the factors of:\n"))
        print("FACTORS ARE:")
        for i in range(1, num + 1):
            if num % i == 0:
                print(i)

    elif choice == 4:
        print("Exiting program.")
        break
