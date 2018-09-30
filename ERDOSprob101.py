a = [66,42,24]
for i in range(0,3) :
    power[i] = 0
    b = 3
    k = b
    while a[i]//k > 0 :
        power[i] = a[i]//k + power[i]
        print(a[i]//k)
        k = k*b
    print(a[i],power[i])
print(power[0]-power[1]-power[2])
    
    
    
