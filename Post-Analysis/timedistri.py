#coding=utf-8

import numpy as np 


xvg = 'coord.xvg'
fp = open(xvg)
coord = []
for ii in fp:
    coord.append(list(map(float,ii.split()[1:])))
#print (coord)
cooarray=np.array(coord)
rows,cols=cooarray.shape
w = 0
x = 0
y = 0
z = 0
otime = np.zeros(cols,dtype=int)
for i in range (cols):
    for j in range (rows):
        if cooarray[j][i]<5.9 and cooarray[j][i]>0:
            w+=1
            otime[i]+=1
        elif cooarray[j][i]<6.644 and cooarray[j][i]>=5.9:
            x+=1
            otime[i]+=1
        elif cooarray[j][i]<8.069 and cooarray[j][i]>=6.644: 
            y+=1
            otime[i]+=1
        elif cooarray[j][i]<9.344 and cooarray[j][i]>=8.069: 
            z+=1
            otime[i]+=1
print (w,x,y,z,otime)