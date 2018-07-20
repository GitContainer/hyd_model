# a is R1 and b is 2*R2

def A(a,b):
    A=(22/7)*a*b*0.5*0.5
    print("\n Area of the half Ellipse: {}".format(A))
    w=A/4.45
    print(" Width: {}".format(w))
    print(" Height: 4.45")
    
    return 

a=float(input("a: ").strip())
b=float(input("b: ").strip())

A(a,b)
