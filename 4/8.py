N=int(input())

dp=[[0]*10 for i in range(N+1)]
for i in range(0, 10):
    dp[1][i]=1
for n in range(2, N+1):
    for i in range(0, 10):
        if i==0:
            dp[n][i]=dp[n-1][i]+dp[n-1][i+1]
        elif i==9:
            dp[n][i]=dp[n-1][i-1]+dp[n-1][i]
        else:
            dp[n][i]=dp[n-1][i-1]+dp[n-1][i]+dp[n-1][i+1]
ans=0
for i in range(1,10):
    ans+=dp[N][i]
print(ans)
