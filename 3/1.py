#A. Белоснежка и n гномов

#У Белоснежки n гномов, и все они очень разные. Она знает, что для того, чтобы уложить спать i-го гнома нужно ai минут, и после этого он будет спать ровно bi минут. Помогите Белоснежке узнать, может ли она получить хотя бы минутку отдыха, когда все гномы будут спать, и если да, то в каком порядке для этого нужно укладывать гномов спать.

from pickle import FALSE, TRUE


n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]

c=[]
for i in range(n):
    c.append([a[i],b[i],i+1])

c.sort(key=lambda x:x[0]+x[1])
#c.reverse()
#print(c)

ans=TRUE
sum=1
for i in range(n-1):
    if sum+c[i][0]>c[n-1][1] or c[i][1]<sum:
        ans=FALSE
        break
    sum+=c[i][0]
    

if ans==TRUE:
    for i in range(n-1,-1,-1):
        print(c[i][2], end=" ")
else:
    print(-1)





    

