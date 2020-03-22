def circle_area(radius):
   
    pi=3.147
    area=pi* radius *radius
    print (area,    "is the area of the Circle")

def circle_perimeter(radius):
    pi=3.147
    perimeter=2*pi*radius
    print (perimeter,    "is the perimter of the Circle")

def square_area(length):
    area=length*length
    print(area, "is the area of the square")

def square_perimeter(length):
    perimeter=length*4
    print(perimeter, "is the perimeter of the square")

def rectangle_area(length,width):
    area=length*width
    print(area, "is the area of the rectangle")

def rectangle_perimeter(length,width):
    perimeter=(2*length) + (2*width)
    print(perimeter, "is the perimeter of the rectangle")

print("My awesome program can Compute Area and Perimeter of a circle, square rectangle!!!!")
print("Enter the shape:")
shapeName = str(input())
if shapeName.lower()== "circle": 
    print("Enter circle radius,decimal number is allowed:")
    radius = float (input())
    
    #pi = 3.147
    # Area of a circle PI *  R * R (Radius square)
    circle_area(radius)
    #area = pi * radius * radius

    # Perimter of a circle PI *  R  (2 * PI * Radius)
    circle_perimeter(radius)
    #perimter = 2 * pi * radius
    #print (area,    "is the area of the Circle")
    #print (perimter,    "is the perimter of the Circle")
elif shapeName.lower()== "square": 
   
    print("Enter the side of the Square:")
    length = float (input())
    # Area of a square L*  W (l equals w)
    #area =  length * length 
    square_area(length)
    # Perimter of a square 4 *  L 
    square_perimeter(length) 
    #perimter = 4* length 
    #print (area,    "is the area of the Square")
    #print (perimter,    "is the perimter of the Square")
elif shapeName.lower()== "rectangle": 
    print("Enter the length of the Rectangle:")
    length = float (input())
    print("Enter the width of the Rectangle:")
    width= float(input())
    # Area of a rectangle L*  W
    rectangle_area(length,width)
    #area =  length * width
    # Perimter of a rectangle 2 *(w+L) 
    #perimter = 2* (length + width)
    rectangle_perimeter(length,width)
    #print (area,    "is the area of the rectangle")
    #print (perimter,    "is the perimter of the rectangle")
else :
    print ("bad guy >:(")
