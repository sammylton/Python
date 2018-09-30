for N in range(2162160,2162161) :
    C = 1
    for n in range(2,N+1) :
        for i in range(2,n+1) :
            if (n%i) == 0 :
                if i == n :
                    k = N
                    c = 1 # term to be multiplied to get the no. of divisors 
                    while True :
                        if k%i == 0 :
                            c = c + 1
                            k = k/i
                        else :
                            break
                    if c != 1 :
                        C = C*c
                        print(i,'**',c-1)
                else :
                
                    break
    print(N,C)
