data=open('input2.txt',"r")
la=list()
h,d,aim=0,0,0
for x in data:
    la.append(x.strip().split(' '))
print(la[1][0])
for i in range(len(la)):
    if la[i][0]=='forward':
        h+=int(la[i][1])
        d+=aim*int(la[i][1])
    elif la[i][0]=='down':
        aim+=int(la[i][1])
    elif la[i][0]=='up':
        aim-=int(la[i][1])
print(h*d)

