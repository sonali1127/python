#ass2:wap program to print maximum of each column from the matrix
n=int(input())
A=[]
for i in range(n):
    l=list(map(int,input().split()))
    A.append(l)
for i in range(0,n):
    maxx=A[0][i]
    for j in range(0,n):
        if A[j][i]>maxx:
            maxx=A[i][j]
    print(maxx,end=' ')