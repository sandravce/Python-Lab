# get a string from an input string where all occurences of first character replaced with dollar symbol except first character...

word=input("Enter a text :")
text=word[0]
result=text+word[1:].replace(text,'$')
print(result)
    
