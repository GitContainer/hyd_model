'This script converts to semi-circular area to circular area with corresponding diameter'

import math
"Define R"
R=10

A= 0.5*(math.pi*R*R)
R_new=(A/math.pi)**(0.5)
D_new=R_new*2

print('Diameter = %f' %D_new)
