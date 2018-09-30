sum1 = 0
for i in range(123000000,1000000001):
    n = hex(i)[2:]
    z = n[::-1]
    if (n == z):
        m = oct(i)[2:]
        y = m[::-1]
        if (m == y):
            a = bin(i)[2:]
            x = a[::-1]
            if ( a == x):
                print(a,m,n,i)
                sum1 = sum1 + i
print(sum1)
