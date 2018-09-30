import math
c = [0,0,0,0,0,0,0,0,0,0]
# wont work for n = 2,3
for n in range(10**10,10**11) :
    m = (int(math.sqrt(n)))
    for i in range(2,(m)+1) :
        if n%i == 0 :
            break
        elif i == m :
            a = str(n)
            prod_c = 1
            for k in range(0,10) :
                c[k]=0
                for j in a :
                    if j == str(k) :
                        c[k] = c[k]+1
                prod_c = (prod_c)*(c[k])
            if prod_c >= 1 :
                print(n,prod_c)
                break
                          
            
             
