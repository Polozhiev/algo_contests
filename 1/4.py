from audioop import reverse


def MergeTeam(lst, l, mid,r):
    L=[]
    R=[]
    for i in range(mid-l):
        L.append(lst[l+i])
    for i in range(r-mid+1):
        R.append(lst[mid+i])

    pL=0
    pR=0
    pLst=l
    while pL!=mid-l and pR!=r-mid+1:
        if L[pL][0]>R[pR][0]:
            lst[pLst]=L[pL]
            pL+=1
        elif L[pL][0]==R[pR][0]:  
            if L[pL][1]<=R[pR][1]:
              lst[pLst]=L[pL]
              pL+=1  
            else:
                lst[pLst]=R[pR]
                pR+=1                
        else:
            lst[pLst]=R[pR]
            pR+=1
        pLst+=1
    while pL!=mid-l:
        lst[pLst]=L[pL]
        pLst+=1
        pL+=1
    while pR!=r-mid+1:
        lst[pLst]=R[pR]
        pLst+=1
        pR+=1

def SortTeam(lst, l,r):
    if l<r:
        mid=(l+r)//2
        SortTeam(lst, l, mid)
        SortTeam(lst, mid+1, r)
        MergeTeam(lst, l, mid+1,r)


n, k = map(int, input().split())
lst=[]
team=[]
for i in range(n):
    team = [int(a) for a in input().split()]
    lst.append(team)

#print(lst)
#lst.sort()
#lst.reverse()
#print(lst)

SortTeam(lst, 0, len(lst)-1)
#lst.reverse()
#print(lst)
k-=1
i=k
j=k
ans=1
while i<n-1 and lst[k][0]==lst[i+1][0] and lst[k][1]==lst[i+1][1]:
    i+=1
    ans+=1
while j>0 and lst[k][0]==lst[j-1][0] and lst[k][1]==lst[j-1][1]:
    j-=1
    ans+=1

print(ans)
# lst=[1,10,2,4, 20, -4, 0, 122, 133, 124, -500]
# print(lst)
# SortTeam(lst, 0, len(lst)-1)
# print(lst)
