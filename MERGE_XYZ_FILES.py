import os
# Write the folder path includes ".xyz" files ! 
for file in os.listdir("C:\\Users\\eray\Desktop\\TEMP\\SUSURLUK_EK_YERLER\\TAVSANLI\\SHP\\DEM_POINTS\\XYZ\\5M"):
        lines = open(file).readlines()
        open("ALL_5m.xyz", 'a').writelines(lines)
