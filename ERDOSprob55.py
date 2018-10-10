for i in range(77846003,311398605) :
    j = str(i**2)
    #print(j)
    if (int(j)/(10**17)<1.0) :
        j = '0' + j
        print(j)
    k = j[1]+j[3]+j[5]+j[7]+j[9]+j[11]+j[13]+j[15] 
    if k == '66006660' :
        print(i)
        break


