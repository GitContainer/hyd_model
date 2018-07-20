
# This script determines datum for structure outlet crossection.
# For structures that do not have drawing of the geometrty ! ! !

def d(x1,x2,x_str,h1,h2,L):
    Ch_str_1=x_str-(L/2)
    Ch_str_2=x_str+(L/2)
    slope=((h2-h1)/(x2-x1))
    datum=(slope*L)

   
    y1="New chainage for x-section BEFORE the structure= {} m".format(Ch_str_1)
    y2="New chainage for x-section AFTER the structure= {} m".format(Ch_str_2)
    y3="Datum for the x-section AFTER the structure= {} m".format("%.3f" % datum)

    print ("\n")
    print ("########## RESULTS ###########")
    print ("\n \n")
    print ("Slope: {}".format(slope))
    print(y1)
    print("Structure Chainage: {}".format(x_str))
    print(y2)
    print(y3)

    return

x1=float(input("Original x-section chainage before the structure: ").strip())
x2=float(input("Original x-section chainage after the structure: ").strip())
x_str=float(input("Structure chainage: ").strip())
h1=float(input("Lowest elevation at the original x-section BEFORE the structure: ").strip())
h2=float(input("Lowest elevation at the original x-secton AFTER the structure: ").strip())
L=float(input("Length of the structure: ").strip())

d(x1,x2,x_str,h1,h2,L)

print("\n")
print ("###########################################")
print ("\n \n")  
k=input("Press close to exit")    
    
    
    
