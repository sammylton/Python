sum = 0
for i in range(2**30+1,2**30+1001) :
    for j in range(2**30+1,2**30+1001) :
        sum = sum + i^j
print(sum)    
    


