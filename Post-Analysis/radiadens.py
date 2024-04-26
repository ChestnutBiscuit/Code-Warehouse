#coding=utf-8
import numpy as np

trajs = 'nafion.gro'

def get_Nafcoord(tp,keyword,skip=1):
	Nafcoord = []
	ITEM = []
	for ii in tp:#逐行读取坐标
		if keyword in ii:#如果该行内包括keywords
			for jj in tp:
				if skip:
					skip = skip - 1
					continue
				ITEM = list(map(str,jj.split()))
				Nafcoord.append(list(map(float,ITEM[3:6])))
				if len(Nafcoord) == 8166:
					#print(Scoord)
					break
			break
            
	return Nafcoord

tp = open(trajs)
Nafcoord_list = []	
for i in range(1250):
	keyword = 'Nafion'
	Nafcoord = get_Nafcoord(tp,keyword,skip=1)
	Nafcoord_list.append(Nafcoord)
dimen = np.array(Nafcoord_list).shape
#print(dimen)
#print(len(Nafcoord_list))
#print(Nafcoord_list)

densmap = np.zeros((31,119))
for i in range (1250):
    for j in range (8166):
        r = math.floor(math.sqrt((Nafcoord_list[i][j][0]-4.30415)**2+(Nafcoord_list[i][j][1]-3.62100)**2)/0.05)
        z = math.floor(Nafcoord_list[i][j][2]/0.05)
        densmap[r][z] += 1
        
for i in range (31):
    for j in range (119):
        print (i*0.05,j*0.05,densmap[i][j])