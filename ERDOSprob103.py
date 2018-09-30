n = 7
sum = 0
for i in range(0,2**n,2):
    b = bin(i)[2:]
    l = len(b)
    b = '0'*(n-l)+b
#    print(b)
    b = b.replace('0', '3')
    b = b.replace('1', '7')
#    print(b)    
    k = int(b)
    while k//10 > 0 :
        k = k//10 - 2*(k%10)
    if k%7 == 0 :
        sum = sum + int(b)
    
print(sum)
