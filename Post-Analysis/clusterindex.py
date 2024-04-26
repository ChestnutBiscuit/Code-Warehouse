#coding=utf-8
import numpy as np
import math
from ase.io import read,write
from ase import Atoms,Atom
import glob
import os
from ase.data import chemical_symbols
from pymatgen.io.ase import AseAtomsAdaptor
import itertools


np.set_printoptions(threshold=np.inf)
gro = 'S.gro'
frames = 50
Satoms = 200

def get_block(fp,keyword):
	Coord=[]
	for ii in fp:#逐行读取坐标
		if keyword in ii:#如果该行内包括keywords
			for jj in fp:
				Coord.append(list(map(float,jj.split()[3:6])))
				if len(Coord) == Satoms:
					break
			break

	return Coord
    
def listdiv(list,a):
    index = []
    for i, item in enumerate(list):
        if item == a:
            index.append(i)
            
    return index


#####原子坐标#####
fp = open(gro)
Coord_list = []
for i in range(frames):
	keyword = '  200'
	Coord = get_block(fp,keyword)
	Coord_list.append(Coord)
	#print(len(Coord))
#print(Coord_list)


#####各原子距离矩阵#####
Dista_matrix = np.empty(shape=(frames,Satoms,Satoms))
for x in range (frames):
    for y in range (Satoms-1):
        for z in range (Satoms):
            if Coord_list[x][y][z]> 59:
                Dista_matrix[x][y][z] = 0
                continue
            if z>y:
                Dista = (Coord_list[x][y][0]-Coord_list[x][z][0])**2+(Coord_list[x][y][1]-Coord_list[x][z][1])**2+(Coord_list[x][y][2]-Coord_list[x][z][2])**2
                Dista_matrix[x][y][z] = math.sqrt(Dista)
            Dista_matrix[x][z][0] = z
#print (Dista_matrix)
#print_log.close()


#####各团簇索引#####
Findex_list= []
for x in range (frames):
    min_distance = 0
    while min_distance <= 0.65:
        flag = 1
        for y in range (Satoms):
            for z in range (1,Satoms):
                if Dista_matrix[x][y][z] < 0.1:
                    continue
                #矩阵中存在0元素
                if Dista_matrix[x][y][0] == Dista_matrix[x][z][0]:
                    continue
                #如果已经是同一个团簇不纳入计算
                elif flag == 1:
                    min_distance = Dista_matrix[x][y][z]
                    cluster_1 = y
                    cluster_2 = z
                    flag = 0
                    continue
                #设置初始量
                if Dista_matrix[x][y][z] < min_distance:
                    min_distance = Dista_matrix[x][y][z]
                    cluster_1 = y
                    cluster_2 = z
                #寻找最小值
        #print (min_distance,cluster_1,cluster_2)
        #距离矩阵中不同团簇原子之间最小的距离量
        if min_distance >= 0.65:
            break
        #当不同团簇原子之间的距离比0.65更大时结束循环
        buffer = Dista_matrix[x][cluster_2][0]
        for clusterindex in range(Satoms):
            if Dista_matrix[x][clusterindex][0] == buffer:
                Dista_matrix[x][clusterindex][0] = Dista_matrix[x][cluster_1][0]
        #合并团簇
    cluster_index = []
    for a in range (Satoms):
        cluster_index.append(Dista_matrix[x][a][0])
    Ucluster_index = np.unique(cluster_index)
    index_list = []
    for i in range (len(Ucluster_index)):
        index = listdiv(cluster_index,Ucluster_index[i])
        index_list.append(index)
    Findex_list.append(index_list)
    #print (index_list)
#print (Findex_list)

CB3gro = 'CB3.gro'
fp = open (CB3gro)
CB3index = []
for ii in fp:
    if ('CB3' in ii):
        CB3index.append(int(ii.split()[2]))
print (CB3index)

#rows, cols = np.array(index_list).shape
combine_list = []
for i in range (len(index_list)):
    combine = list(itertools.combinations(index_list[i],2))
    combine_list.append(combine)
print (combine_list)
#将index二二组合
#    for j in range (len(index_list[i])-1):
#        print (CB3index[index_list[i][j+1]],CB3index[index_list[i][j]])

for i in range (len(combine_list)):
    for j in range (len(combine_list[i])):
        print (CB3index[combine_list[i][j][0]],CB3index[combine_list[i][j][1]])

#print_log = open("printlog.txt",'w')
#print (Dista_matrix,file = print_log)
#print_log.close()
	
