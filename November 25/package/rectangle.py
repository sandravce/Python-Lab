def rectangle(length,breadth):
    area=length * breadth
    perimeter=2 * (length + breadth)
    return(area,perimeter)

length=int(input("Enter the length of the rectangle:"))
breadth=int(input("Enter the breadth of the rctangle:"))

area,perimeter=rectangle(length,breadth)
print("Area of rectangle :",area)
print("Perimeter of rectangle :",perimeter)

