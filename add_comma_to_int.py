num=5000000000
lis=[]
length = len(str(num))
for i in reversed(range(length)):
    if i % 3==0 and i>=3:
        lis.append(',')
        lis.append(str(num)[i])
    else:
        lis.append(str(num)[i])

for i in reversed(lis):
    print(i, end="")
