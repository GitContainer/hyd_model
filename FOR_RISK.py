category = open("category.txt").readlines()
with open("a1234.txt", "a") as new:
    
    flag = 1    
    for m in category:

        if flag != m:
            new.write(m)
        flag = m
        
def cal(x) :       # It takes water depth as input, and output is fr.
 if 0<=x<0.5 :
  Z=0.5*x
 elif 0.5<=x<1 :
  Z=0.4-(3-3*x)/10
 elif 1<=x<1.5 :
  Z=0.5-(1.5-x)/5
 elif 1.5<=x<2 :
  Z=0.6-(2-x)/5
 elif 2<=x<3 :
  Z=0.3+0.15*x 
 elif 3<=x<4 :
  Z=0.45+0.1*x
 elif 4<=x<5 :
  Z=0.45+0.1*x
 elif 5<=x<6 :
  Z=0.7+0.05*x
 else :
  Z=1
 return Z
    

    
def cat(x):
    if x == 1:
        z = "Akaryakit"
    elif x == 2:
        z = "Akvaryum"
    elif x == 3:
        z = "Askeri"
    elif x == 4:
        z = "Dini"
    elif x == 5:
        z = "Eczane"
    elif x == 6:
        z = "Egitim"
    elif x == 7:
        z = "Farm"
    elif x == 8:
        z = "Konut"
    elif x == 9:
        z = "Okul"
    elif x == 10:
        z = "Park"
    elif x == 11:
        z = "Resmi"
    elif x == 12:
        z = "Restaurant"
    elif x == 13:
        z = "Saglik"
    elif x == 14:
        z = "Spor"
    elif x == 15:
        z = "Ticaret"
    elif x== 16:
        z = "Train Station"
    elif x == 17:
        z = "Veterinarian"
    else:
        z = "Konut"
    return z
 
        
        
def RISK(x): # It takes F_A_N (normalize FIN) as input, and output is RISK
    if x > 0:
        z = x * 0.5 + 0.5
    else:
        z = 0
    return z

def RSSN(x,y): # It takes Category and RISK as input, and output is RSSN
    SSH = ["Askeri", "Dini", "Egitim", "Okul", "Saglik"]
    if x in SSH:
        z = y * 1.5
    else:
        z = y
    return z

def subasan(x,y):
    if x > 0 and y =="Çırçırçeşme Mh.":
        return 1
    else:
        return 0