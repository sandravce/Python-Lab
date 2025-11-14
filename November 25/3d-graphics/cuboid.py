def cuboid(length,breadth,height):
    area=2 *((length * breadth)+ (breadth * height)+ (height * length))
    perimeter=4 * (length + breadth + height)
    return(area,perimeter)
