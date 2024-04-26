#coding=utf-8
import numpy as np
from ase.io import read,write
from ase import Atoms,Atom
import glob
import os
from ase.data import chemical_symbols
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.analysis.diffusion.aimd.rdf import RadialDistributionFunction


txt = 'CECCOOREIGEN.txt'
trajs = 'dump_iso.lammpstrj'



def get_Scoord(tp,keyword,skip=8):
	Scoord=[]
	ITEM=[]
	for ii in tp:#逐行读取坐标
		if keyword in ii:#如果该行内包括keywords
			for jj in tp:
				if skip:
					skip = skip - 1
					continue
				#if 'CEC_COORDINATE' in jj:
					#continue
				#print(jj)
				ITEM = list(map(float,jj.split()[:6]))
				if ITEM[1]==19:
					Scoord.append(list(map(float,jj.split()[3:])))
				if len(Scoord) == 39:
					#print(Scoord)
					break
			break
            
	return Scoord

tp = open(trajs)   
Scoord_list = []	
for i in range(2501):
	keyword = 'ITEM: TIMESTEP'
	Scoord = get_Scoord(tp,keyword,skip=8)
	Scoord_list.append(Scoord)
dimen = np.array(Scoord_list).shape
print(dimen)
#print(len(Scoord_list))
#print(Scoord_list)

def get_CECcoord(fp,keyword,skip=0):
	CECcoord=[]
	for ii in fp:
		if keyword in ii:
			for jj in fp:
				if skip:
					skip = skip - 1
					continue
				if 'CEC_COORDINATE' in jj:
					continue
				CECcoord.append(list(map(float,jj.split()[:3])))
				skip = 4
				if len(CECcoord) == 39:
					dimen4 = np.array(CECcoord).shape
					#print(dimen4)
					#print(CECcoord)
					break
			break

	return CECcoord

fp = open(txt)   
CECcoord_list = []	
for i in range(500001):
	keyword = 'CEC_COORDINATE'
	CECcoord = get_CECcoord(fp,keyword,skip=0)
	CECcoord_list.append(CECcoord)
#print(CECcoord_list)
#dimen3 = np.array(CECcoord_list).shape
#print(dimen3)
#print(len(CECcoord_list))

distance = []
dr = 0.05
rmax = 10 
layer_number = int(rmax/dr)
grf = np.zeros(layer_number, dtype='int')
grb = np.zeros(layer_number, dtype='int')
distance_all = []

for i in range(2501):
    for j in range(39):
        distance = []
        for k in range (39):
            dis = ((CECcoord_list[i*200][j][0]-Scoord_list[i][k][0])**2+(CECcoord_list[i*200][j][1]-Scoord_list[i][k][1])**2+(CECcoord_list[i*200][j][2]-Scoord_list[i][k][2])**2)**0.5
            distance.append(dis)
        distance.sort()
        distance_all.append(distance)
        #dimen4 = np.array(distance_all).shape
        #print(dimen4)
        if i == 0:
            continue
        if distance[0] <= rmax:
            layer = int(distance[0]/dr)
            direction = distance_all[i*39][0]-distance_all[39*(i-1)][0]
            if direction > 0:
                grf[layer] +=1
            else:
                grb[layer] +=1
print(grf)
print(grb)

