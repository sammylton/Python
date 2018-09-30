import math
l = 0
L = int(math.sqrt(2*(10**16)-1))
#print(L)
for n in range(1,L) :
    o = 0
    m = 0
    N = (n+1)**2
    if N%2 == 0 :
        m = (N//2)-1
#        print(m)
    if (N-1)%2 == 0 :
        o = (N-1)//2
#        print(o)
    l = m + o + l
print(l)
   
