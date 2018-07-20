lines=open('maras.txt').readlines()
open('maras5m.txt', 'w').writelines(lines[0:91777957:5])
