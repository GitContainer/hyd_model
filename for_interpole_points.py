lines=open('a123.txt').readlines()
for m, i in enumerate(lines,1):
    with open("a1234.txt","a") as new:
            new.write(i)
            new.write("\n")
        
        
