import numpy as np
from scipy.optimize import leastsq
from scipy.optimize import minimize

trajs = 'product.gro'

def get_coord(tp,keyword,atomnum,skip):
    Coord = []
    ITEM = []
    for ii in tp:
        if keyword in ii:
            for jj in tp:
                if skip:
                    skip = skip-1
                    continue
                coordx = float(jj[20:28])
                coordy = float(jj[28:36])
                coordz = float(jj[36:44])
                Coord.append((coordx,coordy,coordz))
                if len(Coord) == atomnum:
                    break
            break

    return Coord

tp = open(trajs)
Coord_list = []
Nafnum = 10
Nafatom = 892
betanum = 104
H3Onum = 130
SOLnum = 875
ISOnum = 945
atomunm = Nafatom*Nafnum + betanum*147 + H3Onum*4 + SOLnum*3 + ISOnum*12
frame = 100
skip = 1
for i in range (frame):
    keyword = 't='
    Coord = get_coord(tp,keyword,atomunm,skip)
    Coord_list.append(Coord)
#print(Coord_list, file=f )
dimen = np.array(Coord_list).shape
print(dimen, file =f)



    


