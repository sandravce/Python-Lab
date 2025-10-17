print("Area of square,rectangle,triangle and circle using lambda function:\n")
print("area of the square:")
side=int(input("enter the side of the square:\n"))
area=lambda s:s*s
print("area of the square =",area(side))

print("\narea of the rectangle:")
length=int(input("enter the length of the rectangle:\n"))
breadth=int(input("enter the breadth of the rectangl:\n"))
area=lambda length,breadth:length*breadth
print("area of the rectangle=",area(length,breadth))


print("\narea of the triangle:")
length=int(input("enter the length of the triangle:\n"))
height=int(input("enter the height of the triangle:\n"))
area=lambda length,height:0.5*length*height
print("area of the rectangle=",area(length,height))

print("area of the circle:")
radius=int(input("enter the radius of the circle:"))
x=lambda r:3.14*radius*radius
print(x(radius))










