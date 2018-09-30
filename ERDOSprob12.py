fr = open('ERDOSprob12.txt','r')
fw = open('12write.txt','w')
for n in fr :
    k = int(n)
    for i in range(2,k+1):
        if k%i == 0 :
            if i == k :
                fw.write(n)
            else :
                break
fr.close()
fw.close()
            
