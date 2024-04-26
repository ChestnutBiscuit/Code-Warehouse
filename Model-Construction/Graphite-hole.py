#coding=utf-8
import math
import numpy as np
from scipy.optimize import minimize



def printcoord(fp,coord,xedge,yedge,zedge):
    for i in range(len(coord)+2):
        if i == 0:
            print ("CRYST1",str(format(xedge,'.3f')).rjust(8),str(format(yedge,'.3f')).rjust(8),str(format(zedge,'.3f')).rjust(8)," 90.00  90.00  90.00 P 1           1",file=fp)
            continue
        if i == len(coord)+1:
            print ("END",file=fp)
            continue
        print ("ATOM",str(i).rjust(6)," C   MOL X   1",str(format(coord[i-1][0],'.3f')).rjust(11),str(format(coord[i-1][1],'.3f')).rjust(7),str(format(coord[i-1][2],'.3f')).rjust(7)," 0.00  0.00",file=fp)
    fp.close


def GCNTgen(m,d,Hmin):
    r0 = math.sqrt(3)*m*d/(2*math.pi)
    l = int(math.ceil(Hmin/(3*d)))
    coord = [[0,0,r0],[math.sqrt(3)*d/2,d/2,r0],[math.sqrt(3)*d/2,3*d/2,r0],[0,2*d,r0]]
    ma = m-1
    la = l-1
    for i in range(ma):
        for j in range(4):
            xi = coord[j][0]+((i+1)*math.sqrt(3)*d)
            yi = coord[j][1]
            coord.append([xi,yi,r0])
    length = len(coord)
    for i in range(l):
        for j in range(length):
            xi = coord[j][0]
            yi = coord[j][1]+(i+1)*3*d
            coord.append([xi,yi,r0])

    index = len(coord)
    xedge = m*math.sqrt(3)*d
    yedge = (l+1)*3*d
    
    GNT = []
    for i in range(len(coord)):
        if coord[i][1] > Hmin:
            continue
        angle = coord[i][0]/r0
        xi = r0*math.sin(angle)
        yi = coord[i][1]
        zi = r0*math.cos(angle)
        GNT.append([xi,yi,zi])

    return GNT


def Holegen(Grcoordb,d,r1):
    index = len(Grcoordb)
    for i in range(index-1,-1,-1):
        if Grcoordb[i][0]**2+Grcoordb[i][2]**2 < r1*r1:
            del Grcoordb[i]
            continue
    index4 = len(Grcoordb)
    for i in range (index4-1,-1,-1):
        index4 = len(Grcoordb)
        bond = 0
        for j in range (index4):
            if (Grcoordb[i][0]-Grcoordb[j][0])**2+(Grcoordb[i][2]-Grcoordb[j][2])**2 < 1.21*d*d:
                bond = bond + 1 
                continue
        #print bond
        if bond == 2 and Grcoordb[i][0]**2+Grcoordb[i][2]**2 < 2*r1**2:
            del Grcoordb[i]
    print ('len(Grcoordb)=',len(Grcoordb),'r1=',r1)

    return Grcoordb


def defectbond(holecoord,d,r1):
    defect = 0
    index5 = len(holecoord)
    print (index5)
    for i in range (index5):
        bond = 0
        if holecoord[i][0]**2+holecoord[i][2]**2 < 2*r1*r1:
            for j in range (index5):
                if (holecoord[i][0]-holecoord[j][0])**2+(holecoord[i][2]-holecoord[j][2])**2 < 1.21*d*d:
                    bond += 1
                    continue
            if bond == 3:
                defect += 1
            print (i,bond,defect)
    g = defect

    return g


def asinangel(x,z,sinangle):
    if x > 0 and z > 0:
        sinangle = math.asin(sinangle)
    if x > 0 and z < 0:
        sinangle = math.pi - math.asin(sinangle) 
    if x < 0 and z < 0:
        sinangle = math.pi - math.asin(sinangle)
    if x < 0 and z > 0:
        sinangle = 2*math.pi + math.asin(sinangle)
    return sinangle


def ranklist(posCNT,poshole):
    posholeback = poshole[0:]
    indexlist = len(posCNT)
    rankhole = [] 
    for i in range(indexlist):
        distancelist = []
        for j in range(len(posholeback)):
            distance = (posCNT[i][0]-posholeback[j][0])**2+(posCNT[i][1]-posholeback[j][1])**2+(posCNT[i][2]-posholeback[j][2])**2
            distancelist.append(distance)
        minindex = distancelist.index(min(distancelist))
        rankhole.append((posholeback[minindex][0],posholeback[minindex][1],posholeback[minindex][2]))
        del posholeback[minindex]
    print (rankhole)
    return rankhole
    
    
def disvec(a,b,c,d,e,f):
    disvec = math.sqrt((a-d)**2+(b-e)**2+(c-f)**2)
    return disvec


def func(theta,posCNT,poshole,r0,d):
    theta = theta.reshape((len(theta),1))
    results = 0
    indexDe = len(posCNT)
    print (indexDe)
    Li = theta[0]
    angleCNT1 = theta[1]
    for i in range(indexDe):
        r = math.sqrt(poshole[i][0]**2+poshole[i][2]**2)
        angle = (r0+Li-r)/Li 
        rU = r+Li-Li*math.sin(angle)
        angleG = asinangel(poshole[i][0],poshole[i][2],poshole[i][0]/r)
        Grax = rU*(poshole[i][0]/r)
        Gray = Li-Li*math.cos(angle)
        Graz = rU*(poshole[i][2]/r)
        angleCNT = asinangel(posCNT[i][0],posCNT[i][2],posCNT[i][0]/r0)
        CNTx = r0*math.sin(angleCNT+angleCNT1)
        CNTy = posCNT[i][1]+Li
        CNTz = r0*math.cos(angleCNT+angleCNT1)
        distancevec = disvec(Grax,Gray,Graz,CNTx,CNTy,CNTz)
        if CNTy-Gray>0:
            results = results+(distancevec-d)**2+r0*r0*(angleCNT+angleCNT1-angleG)**2
            continue
        if CNTy-Gray<0:
            results = results+(distancevec-d)**2+r0*r0*(angleCNT+angleCNT1-angleG)**2+10*(CNTy-Gray)**2
            continue        
    return results
    

Hmin = 50
rmin = 15
d = 1.42
val = math.pi
nx = 34
ny = 16

##########################################################
######################graphite generation#################
##########################################################
Gcoord = [[0,0,0],[math.sqrt(3)*d/2,0,d/2],[math.sqrt(3)*d/2,0,3*d/2],[0,0,2*d]]
for i in range(nx):
    for j in range(4):
        xi = Gcoord[j][0]+((i+1)*math.sqrt(3)*d)
        zi = Gcoord[j][2]
        Gcoord.append([xi,0,zi])
        #print(i,j,coord)
Glength = len(Gcoord)
#print (length)
for i in range(ny):
    for j in range(Glength):
        xi = Gcoord[j][0]
        zi = Gcoord[j][2]+(i+1)*3*d
        Gcoord.append([xi,0,zi])
#origin position change#
index = len(Gcoord)
Grcoord = []
for i in range(index):
    xi = Gcoord[i][0]-(nx+1)*math.sqrt(3)*d/2
    zi = Gcoord[i][2]-(ny+1)*3*d/2
    Grcoord.append([xi,0,zi])

xedge = (nx+1)*math.sqrt(3)*d/2
yedge = 80
zedge = (ny+1)*3*d/2
fp = open('graphite.pdb',"w")
printcoord(fp,Grcoord,xedge*2,yedge,zedge*2)
#print Grcoord

#########################################################
#####################hole generation#####################
#########################################################
Grcoordb = Grcoord[0:]
a = 0
m = int(math.ceil(2*val*rmin/(math.sqrt(3)*1.33)))
r0 = math.sqrt(3)*m*1.33/(2*math.pi)
print (r0)
r1 = r0
r2 = r0
holecoord = Holegen(Grcoordb,d,r1)
print (len(Grcoord),len(Grcoordb))
g = defectbond(holecoord,d,r1)
xedge = xedge*2
zedge = zedge*2
print (g)
while a == 0:
    if g == m:
        g = defectbond(holecoord,d,r1)
        print (g,r1)
        fp = open('hole.pdb',"w")
        for i in range (len(holecoord)):
            holecoord[i]=((holecoord[i][0]+(nx+1)*math.sqrt(3)*d/2,holecoord[i][1],holecoord[i][2]+(ny+1)*3*d/2))
        printcoord(fp,holecoord,xedge,yedge,zedge)##graphite with hole
        GCNT = GCNTgen(m,1.33,Hmin)
        fp = open('CNT.pdb',"w")
        printcoord(fp,GCNT,xedge,yedge,zedge)##GCNT structure
        for i in range (len(GCNT)):
            GCNT[i]=((GCNT[i][0]+(nx+1)*math.sqrt(3)*d/2,GCNT[i][1]+2.1,GCNT[i][2]+(ny+1)*3*d/2))
        fp = open('all.pdb',"w")
        all = holecoord + GCNT
        printcoord(fp,all,xedge,yedge,zedge)
        break
    if g > m:
        r2 = r2/2
        r1 = r1-r2
        Grcoordb = Grcoord[0:]
        holecoord = Holegen(Grcoordb,d,r1)
        g = defectbond(holecoord,d,r1)
        lenGr = len(Grcoord)
        print ("2",g,m,lenGr)
        continue
    if g < m:
        r2 = r2/2
        r1 = r1+r2
        Grcoordb = Grcoord[0:]
        holecoord = Holegen(Grcoordb,d,r1)
        g = defectbond(holecoord,d,r1)
        lenGr = len(Grcoord)
        print ("3",g,m,lenGr)
        continue

indexNT = len(GCNT)
indexhole = len(holecoord)


#posCNT = []
#for i in range (indexNT-1,-1,-1):
#    if GCNT[i][1] == 0:
#        posCNT.append((GCNT[i][0],GCNT[i][1],GCNT[i][2]))
#        del GCNT[i]
#lenCNT = len(posCNT)
#
#poshole = []
#indexdefect = []
#for i in range (indexhole-1,-1,-1):
#    bond = 0
#    indexhole = len(holecoord)
#    if holecoord[i][0]**2+holecoord[i][2]**2 < 2*r1*r1:
#        for j in range (indexhole):
#            if (holecoord[i][0]-holecoord[j][0])**2+(holecoord[i][2]-holecoord[j][2])**2 < 1.21*d*d:
#                bond += 1
#                continue
#        if bond == 3:
#            poshole.append((holecoord[i][0],holecoord[i][1],holecoord[i][2]))
#            indexdefect.append(i)
#            continue
#lenhole = len(poshole)
#indexdefect.sort(reverse=True)
#for i in range (len(indexdefect)):
#    j = indexdefect[i]
#    del holecoord[j]
#
#print (lenCNT,lenhole,len(indexdefect))
#
##minimize function
#rankhole = ranklist(posCNT,poshole)
#fp = open('poshole.pdb','w')
#printcoord(fp,poshole,xedge,yedge,zedge)
#print (poshole,rankhole,posCNT)
#theta = (1.5,0)
#result=minimize(fun=func,x0=theta,args=(posCNT,rankhole,r0,d),method = 'BFGS')
#print (result)
#
#
#
##########################################################
####################coordination output###################
##########################################################
#final_theta = result.x
#Li = final_theta[0]
#angleCNT1 = final_theta[1]
#posall = []
#for i in range (len(GCNT)):
#    angleCNT = asinangel(GCNT[i][0],GCNT[i][2],GCNT[i][0]/r0)
#    GCNT[i]=((r0*math.sin(angleCNT+angleCNT1),GCNT[i][1]+Li,r0*math.cos(angleCNT+angleCNT1)))
#    posall.append(GCNT[i])
#for i in range (len(holecoord)):
#    posall.append(holecoord[i])
#
#for i in range(m):
#    r = math.sqrt(poshole[i][0]**2+poshole[i][2]**2)
#    angle = (r0+Li-r)/Li 
#    rU = r+Li-Li*math.sin(angle)
#    angleG = asinangel(poshole[i][0],poshole[i][2],poshole[i][0]/r)
#    Grax = rU*(poshole[i][0]/r)
#    Gray = Li-Li*math.cos(angle)
#    Graz = rU*(poshole[i][2]/r)
#    angleCNT = asinangel(posCNT[i][0],posCNT[i][2],posCNT[i][0]/r0)
#    CNTx = r0*math.sin(angleCNT+angleCNT1)
#    CNTy = posCNT[i][1]+Li
#    CNTz = r0*math.cos(angleCNT+angleCNT1)
#    GCNT.append((CNTx,CNTy,CNTz))
#    holecoord.append((Grax,Gray,Graz))
#    posall.append((CNTx,CNTy,CNTz))
#    posall.append((Grax,Gray,Graz))
#    
#fp = open('GCNT.pdb','w')
#printcoord(fp,GCNT,xedge,yedge,zedge)
#fp = open('holecoord.pdb','w')
#printcoord(fp,holecoord,xedge,yedge,zedge)
#fp = open('all.pdb','w')
#printcoord(fp,posall,xedge,yedge,zedge)

