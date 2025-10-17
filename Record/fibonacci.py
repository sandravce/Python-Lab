print("fibonacci series of n terms using function:\n")
def fibonacci(n):
    a = 0
    b = 1
    series = [] 

    for i in range(n):
        series.append(a)
        c = a + b
        a = b
        b = c

    print(tuple(series))  
n_terms = int(input("Enter how many Fibonacci numbers you want: "))
fibonacci(n_terms)


