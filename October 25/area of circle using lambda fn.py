# Find the area of circle using lambda function

radius=int(input("Enter the radius of the circle:"))
pi=3.14
area=lambda pi,radius:pi*radius*radius
print(area(pi,radius))
