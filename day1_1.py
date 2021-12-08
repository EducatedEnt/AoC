data = open("input1.txt",'r')
lala=list()
for x in data:
    lala.append(int(x.strip()))
count=0
for i in range(1,len(lala)):
    if i>1900:
        print(i)
    if lala[i]>lala[i-1]:
        count+=1
print(count)
data.close()