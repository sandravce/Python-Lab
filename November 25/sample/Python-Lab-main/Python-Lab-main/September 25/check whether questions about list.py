list1=[1,2,3,4,5,6,7]
list2=[2,4,6,8,10]

a=len(list1)
print("Length of first list is :",a)

b=len(list2)
print("Length of second list  is :",b)

if(a==b):
     print("Length are same")
else:
    print("Length are not same\n")

c=sum(list1)
print("sum =",c)

d=sum(list2)
print("Sum =",d)

if(c==d):
    print("Sum is not equal")
else:
    print("Sum is not equal\n")

for i in list1:
    for j in list2:
        if(i==j):
            print(i)

