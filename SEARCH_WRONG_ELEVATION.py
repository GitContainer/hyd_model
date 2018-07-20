lines=open('ALL_5m.xyz').readlines()
for m in lines:
    n = m.split()
    q3 = float(n[2])
    
    if q3 < 500:
        print m
 
   