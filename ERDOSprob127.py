n = 4444444444/(4**16)
count = 17 # no of nos under parent odd 1
p = 17 # no of nos under parent odd no (here 1) 
j = []
# count of odd numbers 
for i in range(0,17,1) :
    m = int(n*(4**i))
    j.append(m) 
    print(i,j[i],p-i-1)
