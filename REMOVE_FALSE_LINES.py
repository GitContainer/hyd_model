false_keys=['-']

with open('maras5m_v1.txt') as oldfile, open ('newfile.txt', 'w') as newfile:
    for line in oldfile:
        if not any(false_key in line for false_key in false_keys):
            newfile.write(line)
