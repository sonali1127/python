'''ass2:wap to duplicate odd numbers from the list
ex:input:6 7 2 5 9 1 33 74
output:6 7 7 2 5 5 9 9 1 1 33 33 74'''
l=list(map(int,input().split()))
res=[]
for i in l:
    if i%2==0:
        res.append(i)
    else:
        res.append(i)
        res.append(i)
for i in res:
    print(i,end=" ")