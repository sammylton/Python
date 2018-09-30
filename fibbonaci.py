a1 = 1
a2 = 1
n = 40
for i in range(3,n+1) :
    a3 = a1 + a2
    a1 = a2
    a2 = a3
#    print(a3)
    if i%2 == 1 and i > 3 :
        print(i,a3)
        for j in range(2,(a3)+1) :
            if (a3)%j == 0 :
                if j >= a3 :
                    print(i,a3)
                else :
                    for k in range(2,(a3)//2 +1) :
                        if ((a3)%k) == 0 :
                            print((a3)//k)
