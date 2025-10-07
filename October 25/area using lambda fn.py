# Find the area of circle using lambda function

radius=int(input("Enter the radius of the circle:"))
pi=3.14
area=lambda pi,radius:pi*radius*radius
print(area(pi,radius))
print() # new line

# Find the area of square using lambda function

length=int(input("Enter the length of the square:"))
area=lambda length:length*length
print(area(length))
print() # new line

# Find the area of rectangle using lambda function

length=int(input("Enter the length of the rectangle:"))
breadth=int(input("Enter the breadth of the rectangle:"))
area=lambda length,breadth:length*breadth
print(area(length,breadth))
print() # new line

# Find the area of triangle using lambda function

base=int(input("Enter the base of the triangle:"))
height=int(input("Enter the height of the triangle:"))
area=lambda base,height:0.5*base*height
print(area(base,height))
print() # new line











