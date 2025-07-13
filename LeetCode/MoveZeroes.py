num = [0, 1, 0, 3, 12, 0]

j=0
for i in range(len(num)):
    if num[i]!=0:
        num[i],num[j]=num[j],num[i]
        j+=1
print(num)