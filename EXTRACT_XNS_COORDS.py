lines=open('MUSTAFAKEMALPASA.txt').readlines()

with open("XNSCOORDS.txt", "w") as new:
    for i, m in enumerate (lines,1):
        if m == "COORDINATES\n":
            c = i+1
            for j, n in enumerate(lines,1):
                if c==j:
                    new.write(n)