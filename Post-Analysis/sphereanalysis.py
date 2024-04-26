import numpy as np
from scipy.optimize import leastsq
from scipy.optimize import minimize
from numpy.linalg import svd
import math

trajs = 'nopbc.gro'

##################################################################################
'''------                      获取gro文件单帧坐标                       -------'''
##################################################################################
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


###################################################################################
'''------          通过一组三维点拟合一个球体，并返回球心坐标和半径          -------'''
###################################################################################
def sphere_fit(Coord_list,frame,molindex,atomindex,betastart,interval):

    ### 定义优化的目标函数
    def objective(x):
        xc, yc, zc, r = x
        distances = np.sqrt((points[:, 0] - xc)**2 + (points[:, 1] - yc)**2 + (points[:, 2] - zc)**2)

        return np.sum((distances - r)**2)
    
    x = [Coord_list[frame][betastart+molindex*147+atomindex][0],Coord_list[frame][betastart+molindex*147+atomindex+interval*1][0],Coord_list[frame][betastart+molindex*147+atomindex+interval*2][0],Coord_list[frame][betastart+molindex*147+atomindex+interval*3][0],Coord_list[frame][betastart+molindex*147+atomindex+interval*4][0],Coord_list[frame][betastart+molindex*147+atomindex+interval*5][0],Coord_list[frame][betastart+molindex*147+atomindex+interval*6][0]]
    y = [Coord_list[frame][betastart+molindex*147+atomindex][1],Coord_list[frame][betastart+molindex*147+atomindex+interval*1][1],Coord_list[frame][betastart+molindex*147+atomindex+interval*2][1],Coord_list[frame][betastart+molindex*147+atomindex+interval*3][1],Coord_list[frame][betastart+molindex*147+atomindex+interval*4][1],Coord_list[frame][betastart+molindex*147+atomindex+interval*5][1],Coord_list[frame][betastart+molindex*147+atomindex+interval*6][1]]
    z = [Coord_list[frame][betastart+molindex*147+atomindex][2],Coord_list[frame][betastart+molindex*147+atomindex+interval*1][2],Coord_list[frame][betastart+molindex*147+atomindex+interval*2][2],Coord_list[frame][betastart+molindex*147+atomindex+interval*3][2],Coord_list[frame][betastart+molindex*147+atomindex+interval*4][2],Coord_list[frame][betastart+molindex*147+atomindex+interval*5][2],Coord_list[frame][betastart+molindex*147+atomindex+interval*6][2]]
    points = np.column_stack((x, y, z)) # 七个点的坐标
    inital_guess = np.append(np.mean(points, axis=0), np.std(points)) # 初始猜测值：球心坐标为点集中心，初始半径为点到中心的平均距离
    print (inital_guess)
    result = minimize(objective, inital_guess)

    if result.success:
        xc, yc, zc, r = result.x
        return r
    else:
        return 0

###################################################################################
'''------                    计算分子质心与环状平面夹角                    -------'''
###################################################################################   

### 计算分子质心
def cal_centroid(Coord_list, frame, molindex, molnum, betastart, f):
    x, y, z = [], [], []
    for i in range (molnum):
        x.append(Coord_list[frame][betastart + molindex*molnum + i][0])
        y.append(Coord_list[frame][betastart + molindex*molnum + i][1])
        z.append(Coord_list[frame][betastart + molindex*molnum + i][2])
    points = np.column_stack((x, y, z))
    print (points, file = f)
    centroid = np.mean(points, axis=0)

    return points, centroid


### 计算一组三维点最佳拟合平面的法向量
def best_fit_plane(points):
    centroid = np.mean(points, axis=0) # 点集质心
    cov_matrix = np.cov((points - centroid).T) # 去中心化后的点集的协方差矩阵
    _, _, Vt = svd(cov_matrix) # 协方差矩阵特征值分解
    normal = Vt[-1] # 最小特征值对应特征向量为平面法向量
    
    return normal


### 计算两个向量之间夹角，以度为单位
def angle_between_vectors(v1, v2):
    dot_product = np.dot(v1, v2) # 向量点积
    norm_v1 = np.linalg.norm(v1) # v1向量模
    norm_v2 = np.linalg.norm(v2) # v2向量模
    cos_angle = dot_product / (norm_v1 * norm_v2) # 计算夹角余弦值
    angle_rad = np.arccos(cos_angle) * (180.0 / np.pi) # 计算与法向量夹角（弧度转换为度）
    # 转换为与平面的夹角
    if angle_rad > np.pi /2:
        angle = angle_rad - np.pi /2
    else:
        angle = np.pi / 2 - angle_rad
 
    return angle*(180.0 / np.pi)


### 求环糊精附近溶剂与质心的夹角与距离
def cal_angdis(Coord_list, frame, cennum, cenatom, censtart, refnum, refatom, refstart):
    angles, distances = [], []
    for i in range(frame):
        for j in range(cennum):
            neighbor_list = []
            pointscen, centroidcen = cal_centroid(Coord_list, i, j, cenatom, censtart, f) # 求第j+1个中心分子的点集和中心
            #print (centroidcen, file = f)
            oring_index = [35, 36, 37, 38, 39, 40, 41] # oring在环糊精分子中的index
            oring_points = pointscen[oring_index, :]
            vector1 = best_fit_plane(oring_points) # oring的最佳拟合平面
            for k in range(refnum):
                pointsref, centroidref = cal_centroid(Coord_list, i, k, refatom, refstart, f) # 求k+1个参考分子的点集合中心
                #print (centroidref, file =f)
                distance = math.sqrt((centroidcen[0]-centroidref[0])**2+(centroidcen[1]-centroidref[1])**2+(centroidcen[2]-centroidref[2])**2) # 中心分子中心与参考分子中心的距离
                if distance < 1.2:
                    Coord_vector = [centroidcen[i]-centroidref[i] for i in range (len(centroidref))] # 距离向量
                    angle = angle_between_vectors(vector1, Coord_vector)
                    #print (distance, file =f)
                    angles.append(angle)
                    distances.append(distance)
    #print(angles,distances,file = f)

    return angles, distances



####### 获取多帧gro坐标
f = open('test.txt','w')
tp = open(trajs)
Coord_list = []
Nafnum, betanum, H3Onum, SOLnum, ISOnum = 10, 104, 130, 875, 945
Nafatom, betaatom, H3Oatom, SOLatom, ISOatom = 892, 147, 4, 3, 12
atomunm = Nafatom*Nafnum + betanum*betaatom + H3Onum*H3Oatom + SOLnum*SOLatom + ISOnum*ISOatom
frame = 50
skip = 1
for i in range (frame):
    keyword = 't='
    Coord = get_coord(tp,keyword,atomunm,skip)
    Coord_list.append(Coord)
#print(Coord_list, file=f )
dimen = np.array(Coord_list).shape
print(dimen, file =f)

####### 求环糊精分子环状大小
#betastrat = Nafatom*Nafnum
#Rlarge_list=[]
#ROsmall_list=[]
#RCsmall_list=[]
#Rring_list=[]
#inital_guess = [0,0,1]
#for i in range (frame):
#    for j in range (betanum):
#        Rlarge_list.append(sphere_fit(Coord_list, i, j, 0, betastrat, 4 ))
#        ROsmall_list.append(sphere_fit(Coord_list, i, j, 42, betastrat, 2))
#        RCsmall_list.append(sphere_fit(Coord_list, i, j, 56, betastrat, 13))
#        Rring_list.append(sphere_fit(Coord_list, i, j, 35, betastrat, 1))

#print (Rlarge_list,file =f)
#print (ROsmall_list,file =f)
#print (RCsmall_list,file =f)
#print (Rring_list,file =f)

####### 计算中心分子和参考分子的角度和距离
betastart, H3Ostart = Nafnum*Nafatom, Nafnum*Nafatom+betanum*betaatom
SOLstart, ISOstart = H3Ostart+H3Onum*H3Oatom, H3Ostart+H3Onum*H3Oatom+SOLnum*SOLatom
H3Oangles, H3Odistance = cal_angdis(Coord_list, frame, betanum, betaatom, betastart, H3Onum, H3Oatom, H3Ostart)
SOLangels, SOLdistance = cal_angdis(Coord_list, frame, betanum, betaatom, betastart, SOLnum, SOLatom, SOLstart)
ISOangels, ISOdistance = cal_angdis(Coord_list, frame, betanum, betaatom, betastart, ISOnum, ISOatom, ISOstart)
print (H3Oangles, H3Odistance, SOLangels, SOLdistance, ISOangels, ISOdistance, file = f, sep = '\n')
#print (H3Oangles, H3Odistance, file = f, sep = '\n')

