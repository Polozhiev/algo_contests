from collections import defaultdict

def BinsearchInvR(lst, val):
    l=-1
    r=len(lst)
    while r-l>1:
        m=(l+r)//2
        if (lst[m]<=val):
            l=m
        else:  
            r=m
    return l

def BinsearchInvL(lst, val):
    l=-1
    r=len(lst)
    while r-l>1:
        m=(l+r)//2
        if (lst[m]<val):
            l=m
        else:  
            r=m
    return l    

# tmp=[4,5, 8, 14, 16]
# print(BinsearchInv(tmp, 14))
# print(BinsearchInv(tmp, 9))

n=int(input())
towns=[int(a) for a in input().split()]
q=int(input())
req=[]
for i in range(q):
    l = [int(a) for a in input().split()]
    req.append(l)

ind=list(range(n))
d=defaultdict(list)
for key, value in zip(towns, ind):
    d[key].append(value)

#print(d)

ans=""
for i in range(q):
    if req[i][2] in d:
        r=BinsearchInvR(d[req[i][2]], req[i][1]-1)
        l=BinsearchInvL(d[req[i][2]], req[i][0]-1)
        if r==l:
            ans+="0"    
        else:
            ans+="1"
    else:
        ans+="0"
print(ans)


# 6
# 123 666 666 314 434 123
# 9
# 2 2 666
# 1 5 314
# 1 5 578
# 2 4 666
# 4 4 713
# 1 1 123
# 4 5 434
# 2 6 123
# 1 2 666
