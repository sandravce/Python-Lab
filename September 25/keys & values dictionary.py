# write a python program to print a dictionary where the keys are the numbers between 1 and 5 and the values are the square of the keys

print("Square of keys in a dictionary")

n=int(input("Enter a number:\n"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
if n<=15:
    print(d)
