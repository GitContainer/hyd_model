import os
# Write the folder path includes ".xyz" files ! 
for file in os.listdir("C:\Users\eray\Desktop\TEMP\SUSURLUK_EK_YERLER\TAVSANLI\SHP\DEM_POINTS\XYZ"):
    if "_5m" not in file and ".xyz" in file:
        num_lines=sum(1 for line in open(file))
        num = num_lines

        lines = open(file).readlines()
        file2 = file.strip(".xyz")
        open(file2 + "_5m.xyz", 'w').writelines(lines[0:num:5])
