k=int(input())
m=0
n=k
while n!= 0 :
    m=(n%10)+m*10
    n=n//10
print(m+k)
