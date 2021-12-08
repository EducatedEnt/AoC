data = open("input1.txt",'r')
lala=list()
for x in data:
    lala.append(int(x.strip()))
count=0
for i in range(3,len(lala)):
    if lala[i-3]<lala[i]:
        count+=1
print(count)