seq1=input()
seq2=input()

n=len(seq1)
m=len(seq2)
dp=[[0]*(m+1) for i in range(n+1)]


dp[0][0], dp[1][0], dp[0][1]=0,0,0

for i in range(1,n+1):
    dp[i][0]=i
for j in range(1,m+1):
    dp[0][j]=j

for i in range(1,n+1):
    for j in range(1,m+1):
        if seq1[i-1]==seq2[j-1]:
            dp[i][j]=min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1])
        else:
            dp[i][j]=min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1]+1)

print(dp[n][m])