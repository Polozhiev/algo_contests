S, n=map(int, input().split())
weights=[int(i) for i in input().split()]

dp=[[0]*(S+1) for i in range(n+1)]

for i in range(1,n+1):
    for s in range(1,S+1):
        if s>=weights[i-1]:
            dp[i][s]=max(dp[i-1][s], dp[i-1][s-weights[i-1]]+weights[i-1])
        else:
            dp[i][s]=dp[i-1][s]

print(dp[n][S])