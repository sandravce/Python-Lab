#write a program to find the fibonocci series using import functions.
def fibonocci(n):
    a,b=0,1
    fib=[]
    for i in range(n):
        fib.append(str(a))
        a,b=b,a+b
    return "("+",".join(fib) + ")"
n=int(input("Enter number of terms:"))
print(fibonocci(n))
