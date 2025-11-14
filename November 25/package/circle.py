def circle(radius):
    area=3.14 * radius * radius
    circumference=2 * 3.14 * radius
    return(area,circumference)

radius=int(input("Enter the radius of the circle:"))
area,circumference=circle(radius)
print("Area of circle:",area)
print("Circumference:",circumference)
