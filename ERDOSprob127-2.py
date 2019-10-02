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

# a much more simpler code and efficient code
import math
sum1 = 0
a = 4444444444
for i in range(0,20):
    b = 4**i
    c = b*2
    d = (a - b)/(c)
    sum1 = sum1 + (math.floor(d)+1)
    
print(d)
print(sum1)
    
