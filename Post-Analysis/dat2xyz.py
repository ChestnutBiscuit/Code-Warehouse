#coding=utf-8

#dat = 'xdens.dat'
#tp = open(dat)
#
#Nafdens = []
#skip = 1
#for ii in tp:#逐行读取坐标
#    if skip:
#        skip = skip -1
#        continue
#    Nafdens.append(list(map(float,ii.split()[1:])))
#dimen = np.array(Nafdens).shape
#print(dimen)
#
#
#for i in range (95,215):
#    for j in range(150,500):
#        print (0.02*i,0.02*j,Nafdens[i][j])
#        
#        
#        
#dat = 'ydens.dat'
#tp = open(dat)
#
#Nafdens = []
#skip = 1
#for ii in tp:#逐行读取坐标
#    if skip:
#        skip = skip -1
#        continue
#    Nafdens.append(list(map(float,ii.split()[1:])))
#dimen = np.array(Nafdens).shape
#print(dimen)
#
#
#for i in range (130,500):
#    for j in range (150,500):
#        print (0.02*i,0.02*j,Nafdens[i][j])
        
dat = '1Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('1Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)

dat = '2Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('2Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)

dat = '3Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('3Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)
            
            
dat = '4Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('4Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)
            
            
dat = '5Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('5Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)
            
            
dat = '6Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('6Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)
                        
            
dat = '7Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('7Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)
                        
            
dat = '8Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('8Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)
                        
            
dat = '9Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('9Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)
                        
            
dat = '10Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('10Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)
                        
            
dat = '11Nafdens.dat'
tp = open(dat)
Nafdens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Nafdens.append(list(map(float,ii.split()[1:])))
with open ('11Nafdens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Nafdens[i][j],file=f)
                        
dat = '1backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('1backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)

dat = '2backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('2backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)

dat = '3backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('3backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)
            
            
dat = '4backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('4backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)
            
            
dat = '5backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('5backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)
            
            
dat = '6backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('6backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)
                        
            
dat = '7backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('7backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)
                        
            
dat = '8backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('8backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)
                        
            
dat = '9backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('9backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)
                        
            
dat = '10backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('10backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)
                        
            
dat = '11backbonedens.dat'
tp = open(dat)
backbonedens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    backbonedens.append(list(map(float,ii.split()[1:])))
with open ('11backbonedens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,backbonedens[i][j],file=f)            
            
            
dat = '1H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('1H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)

dat = '2H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('2H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)

dat = '3H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('3H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)
            
            
dat = '4H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('4H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)
            
            
dat = '5H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('5H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)
            
            
dat = '6H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('6H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)
                        
            
dat = '7H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('7H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)
                        
            
dat = '8H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('8H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)
                        
            
dat = '9H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('9H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)
                        
            
dat = '10H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('10H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)
                        
            
dat = '11H2Odens.dat'
tp = open(dat)
H2Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    H2Odens.append(list(map(float,ii.split()[1:])))
with open ('11H2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,H2Odens[i][j],file=f)
            
            
            
dat = '1Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('1Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)

dat = '2Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('2Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)

dat = '3Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('3Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)
            
            
dat = '4Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('4Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)
            
            
dat = '5Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('5Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)
            
            
dat = '6Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('6Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)
                        
            
dat = '7Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('7Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)
                        
            
dat = '8Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('8Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)
                        
            
dat = '9Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('9Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)
                        
            
dat = '10Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('10Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)
                        
            
dat = '11Odens.dat'
tp = open(dat)
Odens = []
skip = 1
for ii in tp:#逐行读取坐标
    if skip:
        skip = skip -1
        continue
    Odens.append(list(map(float,ii.split()[1:])))
with open ('11Odens.xvg','wt') as f:
    for i in range (0,427):
        for j in range(0,504):
            print (0.02*i,0.02*j,Odens[i][j],file=f)