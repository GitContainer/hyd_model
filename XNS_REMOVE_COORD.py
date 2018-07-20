lines=open('a123.txt').readlines()

with open("a1234.txt", "a") as new:
    for i, m in enumerate (lines,1):
        if m != "COORDINATES\n" and "    2  " not in m:  
            new.write(m)
        elif m == "COORDINATES\n":
            d = 0
            c = i+1
            new.write(m)
            for j, n in enumerate(lines,1):
                if c==j and "   0" not in n:
                   new.write("    0\n")
                   break
            
