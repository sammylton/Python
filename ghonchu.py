def C(x,y):
    if((x-y)>=y):
        s=1
        t=1
        for i in range(y):
            s=s*(x-i)
            t=t*(1+i)
        return (s/t)
    else:
        s=1
        t=1
        for i in range(x-y):
            s=s*(x-i)
            t=t*(1+i)
        return (s/t)
k=0
for i in range(1,12):
    k=k+C(29,i)
print(k)
