# write a menu program witih options containing

# 1.occurence of each word in a sentence
# 2.count the occurence of characters in a word
# 3.display the factors of a given number
# 4.Exit


print("MENU PROGRAM\n")
print("1: Occurence of word in a sentence\n")
print("2: Frequency of characters in a word\n")
print("3: Factors of a number\n")
print("4: Exit\n")

while True:
    choice=int(input("Enter your choice:"))
    if choice>4 or choice<1:
        print("Invalid choice")
    # choice 1

    elif choice==1:
        print("Occurence of word in a sentence:")
        text=input("Enter the sentence:")
        words=text.split()
        count={}
        for w in words:
            count[w]=count.get(w,0)+1
        print(count)
        print("\n")#for new line
        
    # choice 2
    elif choice==2 :
        print("Frequency of characters in a word")
        word=input("Enter a word:")
        count={}
        for ch in word:
           count[ch]=count.get(ch,0)+1
        print(count)
        print("\n")#for new line

    # choice 3    
    elif choice==3 :
        print("Factors of a number")
        num=(int(input("Enter the number:")))
        print("Factors are:")
        for i in range(1, num + 1):
            if num % i == 0 :
                print(i)

    # choice 4
    elif choice==4 :
        print("Exiting program")
        break

