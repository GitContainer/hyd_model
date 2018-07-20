num_lines=sum(1 for line in open('11_1.xyz'))
print(num_lines)
num = num_lines

lines=open('11_1.xyz').readlines()
open('11_1_5m.xyz', 'w').writelines(lines[0:num:5])
