#coding=utf-8

import numpy as np 

xvg = 'oallcoord.xvg'
fp = open(xvg)
coord = []
for ii in fp:
    coord.append(list(map(float,ii.split()[1:])))
cooarray=np.array(coord)
rows,cols=cooarray.shape
print (rows,cols)
J4 = 0
J3 = 0
J2 = 0
otime = np.zeros(cols,dtype=int)
for i in range (cols):
    for j in range (rows):
        if j == rows-1:
            continue
        if cooarray[j][i]>=8.05 and cooarray[j+1][i]<8.05:
            J4+=1
        elif cooarray[j][i]>=6.6 and cooarray[j+1][i]<6.6:
            J3+=1
        elif cooarray[j][i]>=5.88 and cooarray[j+1][i]<5.88:
            J2+=1
print (J4,J3,J2)