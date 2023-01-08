n=int(input())
seq=[int(i) for i in input().split()]
dp=[1]*n
prev=[-1]*n
for i in range(0,n):
    for j in range(0,i):
        if seq[j]<seq[i] and dp[j]+1>dp[i]:
            dp[i]=dp[j]+1
            prev[i]=j
ans=1
for i in range(n):
    ans=max(ans, dp[i])
print(ans)

k=1
for i in range(1, n):
    if dp[i]>dp[k]:
        k=i
j=ans
L=[0]*ans
while k>-1:
    L[j-1]=seq[k]
    j+=-1
    k=prev[k]

for i in range(ans):
    print(L[i], end=" ")

#3, 29, 5, 5, 28, 6
#1, 2,  2, 2, 3, 3
#-1, 0, 0, 0, 2, 2