data=open('input2.txt',"r")
la=list()
h,d=0,0
for x in data:
    la.append(x.strip().split())
for i in range(len(la)):
    if la[i][0]=='forward':
        h+=int(la[i][1])
    elif la[i][0]=='down':
        d+=int(la[i][1])
    elif la[i][0]=='up':
        d-=int(la[i][1])
print(h*d)

