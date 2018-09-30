a1 = 1
a2 = 1
n = 10**10 # no. of fibonacci terms
b = 10**6 # base of division
for i in range(3,n+1) :
    a3 = a1 + a2
    r3 = (a3)%(b)
    r2 = (a2)%(b)
    if r3 == 0 and r2 == 1:
        print(i)
        break
    a1 = a2
    a2 = a3

    
