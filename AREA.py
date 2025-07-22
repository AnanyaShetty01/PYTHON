def circle():
    r=int(input("Enter radius of circle"))
    print("Area of circle is ",3.14*r*r)
    
def square():
    print("Area of square is ",a*a)
    
def triangle():
    b=int(input("Enter the base "))
    h=int(input("Enter the height of triangle "))
    return 0.5*b*h

def rect(a,b):
    return a*b
    
while(True):
    print("1.CIRCLE")
    print("2.SQUARE")
    print("3.TRIANGLE")
    print("4.RECTANGLE")
    print("5.EXIT")
    ch=int(input("Enter your choice "))
    match ch:
        case 1:
            circle()
        case 2:
            a=int(input("Enter side of a square"))
            square(a)
        case 3:
            res=triangle()
            print("Area of triangle is ",res)
        case 4:
            a=int(input("Enter the length of rect"))
            b=int(input("Enter the breadth of rect"))
            res=rect(a,b)
            
    
    