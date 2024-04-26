#coding=utf-8
        
Odes = []
with open('odestination.xvg') as reader:
    for index, line in enumerate(reader):
        if index % 4 == 0:
            Odes.append(list(map(float,line.split())))
print (Odes)

lens = len(Odes)
for i in range (lens):
    while Odes[i][0]> 92.1450:
        Odes[i][0] -= 92.1450
    while Odes[i][0]< 0:
        Odes[i][0] += 92.1450
    while Odes[i][1]> 88.2000:
        Odes[i][1] -= 88.2000
    while Odes[i][1]< 0:
        Odes[i][1] += 88.2000
                
for i in range (lens):
    print("  OR",str(format(Odes[i][0],'.6f')).rjust(17),str(format(Odes[i][1],'.6f')).rjust(16),str(format(Odes[i][2],'.6f')).rjust(16),sep='')