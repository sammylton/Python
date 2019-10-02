for i in range(1,22) :
    for n in range(1,10000) :
        if (int(bin((201413)**n)[2:]))%(int(bin(2**i)[2:])) == 1 :
            print(i,n)
            break
# more simplistic approach 
a = 201413
b = 2**21
for i in range(1,100):
    if (((a**i)%b)==1):
        print(i)
