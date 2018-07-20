

category = open("category.txt").readlines()
with open("a1234.txt", "a") as new:
    
    flag = 1    
    for m in category:

        if flag != m:
            new.write(m)
        flag = m
    
    