n = 4444444444/(4**16)
count = 17 # no of nos under parent odd 1
p = 17 # no of nos under parent odd no (here 1) 
j = [] # nos required so that the count increment changes
# count of odd numbers 
for i in range(0,16+1,1) :
    m = int(n*(4**i))
    j.append(m) 
#    print(i,j[i])
for i in range(0,15+1,1) :
    k = j[i+1]-j[i]
    if (j[i+1] + j[i])%2 == 0 :
        count = count + ((j[i+1] - j[i])//2)*(p - (i+1))
#        print(count)
    if (j[i+1])%2 == 0 and (j[i])%2 == 1 :
        count = count + ((j[i+1] - j[i] - 1)//2)*(p - (i+1))
#        print(count)
    if (j[i+1])%2 == 1 and (j[i])%2 == 0 :
        count = count + ((j[i+1] - j[i] + 1)//2)*(p - (i+1))
#        print(count)
print(count)
