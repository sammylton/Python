import math
L = int(input('enter a no. u want to break into 2 primes:'))
for n in range(2,L) :
    for i in range(2,n+1) :
        if n%i == 0 :
            if i >= n :
                
                m = L - n
                for j in range(2,m+1) :
                    if m%j == 0 :
                        if j >= m :
                            if m >= n : 
                                print(n,m)
                        else :
                            break
            else :
                break
