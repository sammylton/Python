#m, n = [int(x) for x in input('enter the order of the matrix: ').split()]
m = int(input())
n = int(input())
a = []
for i in range(0,m):
    a.append([])
    for j in range(0,n):
        print('enter the', i+1,j+1, 'entry of the system of linear equations')
        a[i].append(float(input()))
for i in range(0,m):
    for j in range(0,n):
        print(a[i][j])
    
