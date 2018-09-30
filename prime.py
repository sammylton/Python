import math
n = int(input('enter a no. : '))
m = (int(math.sqrt(n)))
for i in range(2,(m+1)+1):
    if n == 2 : 
        print('prime')
    else :
        if n%i == 0 :
            print('not prime')
            break
        elif i >= m :
            print('prime')
            break #just because of 2,3(m+1 had to be done),5(prime was being written twice)
