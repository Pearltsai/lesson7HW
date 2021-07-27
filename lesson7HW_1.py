s=[]
x=int(input('學生數量'))
for i in range(x):
    y=int(input('學生成績'))
    s.append(y)
print('最高:',max(s))

print('最低:',min(s))

print('平均:',sum(s)/x)
