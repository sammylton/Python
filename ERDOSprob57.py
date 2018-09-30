for n in range(1,100001) :
    count = 0
    for i in range(n+1,1002) :
        if (3**i)%(10**4) == (3**n)%(10**4) :
            print(n,i)
            count = count + 1
            if count == 2 :
                
                break
