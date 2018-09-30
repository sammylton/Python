n = 27
fact = 1
 
for i in range(1,n+1):
    fact = fact * i
     
print (" ",end="")
f=fact%1000000007
print(f)
