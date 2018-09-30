import math
for N in range(2,19):
    b = math.factorial(N)
    c = int((2*b)**0.5)
    n = 0
    for i in range(2,c+1):
        if ((b/i + (i+1)/2)%1 == 0):
            print(i)
            n = n + 1
    print(N,"-->",n)
    
