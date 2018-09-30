import math
t = int(input())
for i in range(1,t) :
    m = input().split()
    n = input().split()
    
    m = int(m)
    n = int(n)
    m = int(math.sqrt(n))
    for i in range(2,n+1) :
        if n%i == 0 :
            if i >= n :
                print('prime')
            else :
                print('not prime')
                break
