#n = 100
#count = 0
#for a in range(1,n+1) :
#    for b in range(1,n+1) :
#        for c in range(1,n+1) :
#            for d in range(1,n+1) :
#                if a+d == b+c :
#                    count = count +1
#                    break
#print(count)
n = int(input())
p = (n*(n-1)*(2*n-1))//3 + n**2
print(p)
