N=int(input())

variance=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]

dp=[[0]*10 for i in range(N+1)]

for i in range(0, 10):
    dp[1][i]=1

for n in range(2,N+1):
    for i in range(10):
        for j in range(len(variance[i])):
            dp[n][i]+=dp[n-1][variance[i][j]]

ans=0
for i in range(10):
    if i!=0 and i!=8:
        ans+=dp[N][i]

print(ans % 10**9)