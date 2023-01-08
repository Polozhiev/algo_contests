n, S=map(int, input().split())
weights=[int(i) for i in input().split()]
costs=[int(i) for i in input().split()]


dp=[[0]*(S+1) for i in range(n+1)]

for i in range(1,n+1):
    for s in range(1,S+1):
        if s>=weights[i-1]:
            dp[i][s]=max(dp[i-1][s], dp[i-1][s-weights[i-1]]+costs[i-1])
        else:
            dp[i][s]=dp[i-1][s]

#print(dp[n][S])

used=[0]*(n+1)
i=n
s=S
while(dp[i][s]>0):
    if dp[i][s]==dp[i-1][s]:
        i=i-1
    else:
        used[i]=1
        i=i-1
        s=s-weights[i]

print(sum(used))
for i in range(n+1):
    if used[i]==1:
        print(i, end=" ")
