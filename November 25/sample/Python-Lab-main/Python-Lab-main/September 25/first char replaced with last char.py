#Create a string from given string where first and last characters exchanged...

print("First character is replaced within last character\n")

s=input("Enter the string:")
if len(s)<2:
    print(s)
else:
    s=s[-1] +s[1:-1] +s[0]
    print("First and last character exchanged:",s)
