# write a function that takes the length and width of a rectangle and returns the area


# write another function that finds the area of a cube
# bonus challenge: use your first function inside this function!


# write a function that finds the area of a sphere
# hint: you can get `pi` by importing math (google it!)

#SOLUTION    -im assuming square and circle instead of cube and sphere

def area_rec(l,w):
    return l*w

def area_square(side):
    return area_rec(side,side)
    
def area_circle(radius):
    import math
    return math.pi * radius**2      #returns a float with multiple decimal points


#Another way to combine all three functions in a single one is

def calculate_area(shape,length=None,width=None,radius=None):
    if shape == "rectangle":
        return length * width
    elif shape == "square":
        return length **2
    elif shape == "circle":
        import math
        return math.pi * radius**2
    else:
        print("Invalid shape selected! (Valid shapes: rectangle,square,circle)") 
