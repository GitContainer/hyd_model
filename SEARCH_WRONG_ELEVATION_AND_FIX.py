with open('k1-k8_r_5m.xyz','r') as oldfile, open('k1-k8_r_5m_FIX.xyz', 'w') as newfile:
    for line in oldfile:
        n = line.split()
        q3 = float(n[2])
        if q3 > -2:  # DESIRED LOWEST VALUE !
            newfile.write(line)
            